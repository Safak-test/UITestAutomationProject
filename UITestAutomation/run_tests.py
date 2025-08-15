#!/usr/bin/env python3
"""
Test Runner with Dated Reporting
"""
import os
import sys
import subprocess
import argparse
from utils.report_utils import create_dated_report_path, get_report_metadata

def run_tests_with_dated_reports(markers=None, parallel=False, browser="chrome"):
    """Run tests with dated report folders"""
    
    # Create dated report path
    report_path = create_dated_report_path()
    metadata = get_report_metadata()
    
    print(f"🚀 Starting test execution...")
    print(f"📅 Date: {metadata['date']}")
    print(f"⏰ Time: {metadata['timestamp']}")
    print(f"📁 Report Path: {report_path}")
    print(f"🌐 Browser: {browser}")
    print(f"🏷️  Markers: {markers or 'All tests'}")
    print("-" * 50)
    
    # Build pytest command
    cmd = ["pytest"]
    
    # Add markers if specified
    if markers:
        cmd.extend(["-m", markers])
    
    # Add parallel execution
    if parallel:
        cmd.extend(["-n", "auto"])
    
    # Add HTML report
    html_report_path = os.path.join(report_path, "report.html")
    cmd.extend(["--html", html_report_path, "--self-contained-html"])
    
    # Add Allure report
    allure_results_path = os.path.join(report_path, "allure-results")
    cmd.extend(["--alluredir", allure_results_path])
    
    # Add metadata to environment
    env = os.environ.copy()
    env["TEST_ENV"] = "local"
    env["BROWSER"] = browser
    env["REPORT_PATH"] = report_path
    
    try:
        # Run tests
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:")
            print(result.stderr)
        
        # Print summary
        print("-" * 50)
        print(f"✅ Test execution completed!")
        print(f"📊 HTML Report: {html_report_path}")
        print(f"📈 Allure Results: {allure_results_path}")
        print(f"🔗 View Allure Report: allure serve {allure_results_path}")
        
        # Create summary file
        create_summary_file(report_path, metadata, result.returncode)
        
        return result.returncode
        
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

def create_summary_file(report_path, metadata, exit_code):
    """Create a summary file with test execution details"""
    summary_file = os.path.join(report_path, "test_summary.txt")
    
    with open(summary_file, "w") as f:
        f.write("Test Execution Summary\n")
        f.write("=" * 30 + "\n")
        f.write(f"Date: {metadata['date']}\n")
        f.write(f"Time: {metadata['timestamp']}\n")
        f.write(f"Environment: {metadata['environment']}\n")
        f.write(f"Browser: {metadata['browser']}\n")
        f.write(f"Exit Code: {exit_code}\n")
        f.write(f"Status: {'PASSED' if exit_code == 0 else 'FAILED'}\n")
        f.write(f"Report Path: {report_path}\n")

def main():
    parser = argparse.ArgumentParser(description="Run tests with dated reporting")
    parser.add_argument("--markers", "-m", help="Test markers to run (e.g., smoke, regression)")
    parser.add_argument("--parallel", "-p", action="store_true", help="Run tests in parallel")
    parser.add_argument("--browser", "-b", default="chrome", help="Browser to use")
    
    args = parser.parse_args()
    
    # Run tests
    exit_code = run_tests_with_dated_reports(
        markers=args.markers,
        parallel=args.parallel,
        browser=args.browser
    )
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main() 