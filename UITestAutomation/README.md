# UI Test Automation Project

Bu proje, Selenium WebDriver kullanarak UI testlerini otomatize etmek için geliştirilmiş profesyonel bir test framework'üdür.

## 🚀 Özellikler

- **Page Object Model (POM)** - Sürdürülebilir test yapısı
- **Configuration Management** - Environment-based konfigürasyon
- **WebDriver Factory** - Multi-browser desteği
- **Test Data Management** - Merkezi test verisi yönetimi
- **Pytest** framework entegrasyonu
- **Allure** raporlama sistemi
- **HTML** test raporları
- **Screenshot** alma özelliği
- **Parallel test execution** desteği
- **Cross-browser testing** (Chrome, Firefox, Edge)
- **Mobile testing** desteği
- **CI/CD Pipeline** (GitHub Actions)
- **Docker** desteği
- **Logging** sistemi
- **Error Handling** ve retry mekanizmaları
- **📅 Tarihli Raporlama** - Test geçmişini takip etme
- **⏰ Test Metadata** - Başlangıç/bitiş zamanları
- **📊 Otomatik Klasör Organizasyonu**

## 📋 Gereksinimler

- Python 3.8+
- Chrome Browser
- ChromeDriver

## 🛠️ Kurulum

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd UITestAutomation
```

2. **Virtual environment oluşturun:**
```bash
python -m venv .venv
```

3. **Virtual environment'ı aktifleştirin:**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

## 🧪 Testleri Çalıştırma

### 🆕 **Tarihli Raporlama ile (Önerilen)**

#### Python Script ile:
```bash
# Tüm testleri çalıştır
python run_tests.py

# Smoke testleri
python run_tests.py --markers smoke

# Regression testleri
python run_tests.py --markers regression

# Parallel execution
python run_tests.py --parallel

# Belirli browser ile
python run_tests.py --browser chrome
```

#### Windows Batch Script ile:
```bash
# Tüm testleri çalıştır
run_tests.bat

# Parametrelerle
run_tests.bat --markers smoke --parallel
```

### 📊 **Klasik Yöntemler**

#### Tüm testleri çalıştırma:
```bash
pytest
```

#### Belirli testleri çalıştırma:
```bash
# Smoke testleri
pytest -m smoke

# UI testleri
pytest -m ui

# Regression testleri
pytest -m regression
```

#### Parallel test execution:
```bash
pytest -n auto
```

#### Verbose output ile:
```bash
pytest -v
```

## 📊 Raporlar

### 📅 **Tarihli Rapor Yapısı**
```
reports/
├── 2024-08-14/                    # Tarih klasörü
│   ├── 20240814_134523/           # Zaman damgası klasörü
│   │   ├── report.html            # HTML raporu
│   │   ├── allure-results/        # Allure sonuçları
│   │   └── test_summary.txt       # Test özeti
│   └── 20240814_143012/           # Başka bir test çalıştırması
└── 2024-08-15/                    # Başka bir gün
```

### HTML Raporu:
Testler çalıştırıldıktan sonra HTML raporu tarihli klasörde oluşturulur.

### Allure Raporu:
1. **Allure raporu oluşturun:**
```bash
allure serve reports/2024-08-14/134523/allure-results
```

2. **Allure raporu HTML olarak generate edin:**
```bash
allure generate reports/2024-08-14/134523/allure-results --clean -o reports/2024-08-14/134523/allure-report
```

### 📈 **Test Metadata**
Her test çalıştırmasında şu bilgiler kaydedilir:
- ✅ Test başlangıç zamanı
- ✅ Test bitiş zamanı
- ✅ Test süresi
- ✅ Browser bilgisi
- ✅ Environment bilgisi
- ✅ Test sonuçları

## 📁 Proje Yapısı

```
UITestAutomation/
├── tests/                    # Test dosyaları
│   └── test_google_pom.py   # Google testleri (POM)
├── utils/                   # Yardımcı fonksiyonlar
│   └── report_utils.py      # Raporlama yardımcıları

├── reports/                  # Test raporları (tarihli)
├── requirements.txt          # Python bağımlılıkları
├── pytest.ini              # Pytest konfigürasyonu
├── run_tests.py            # Tarihli test runner
├── run_tests.bat           # Windows batch script
└── README.md               # Bu dosya
```

## 🏷️ Test Markers

- `@pytest.mark.smoke` - Smoke testleri
- `@pytest.mark.regression` - Regression testleri
- `@pytest.mark.ui` - UI testleri
- `@pytest.mark.slow` - Yavaş çalışan testler

## 🔧 Konfigürasyon

Pytest ayarları `pytest.ini` dosyasında tanımlanmıştır:

- Test dosyaları: `test_*.py`
- Test sınıfları: `Test*`
- Test fonksiyonları: `test_*`
- HTML rapor: `reports/report.html`
- Allure sonuçları: `reports/allure-results`

## 📝 Test Yazma

Yeni test eklemek için:

1. `tests/` klasöründe yeni test dosyası oluşturun
2. Test sınıfını `Test*` ile başlatın
3. Test metodlarını `test_*` ile başlatın
4. Uygun marker'ları ekleyin
5. Allure decorator'larını kullanın
6. Test metadata'sını ekleyin

### Örnek Test:
```python
import pytest
import allure
import datetime

@allure.epic("Feature Name")
@allure.feature("Sub Feature")
class TestExample:
    
    @allure.story("Test Story")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_example(self, driver):
        test_start_time = datetime.datetime.now()
        
        with allure.step("Test step"):
            # Test logic here
            pass
        
        test_end_time = datetime.datetime.now()
        test_duration = test_end_time - test_start_time
        allure.attach(
            f"Test Duration: {test_duration}",
            name="test_metadata",
            attachment_type=allure.attachment_type.TEXT
        )
```

## 📊 Test Geçmişi Takibi

### Tarihli Raporlama Avantajları:
- ✅ **Zaman Takibi**: Her test çalıştırması tarihli klasörde
- ✅ **Geçmiş Karşılaştırma**: Farklı zamanlardaki sonuçları karşılaştırma
- ✅ **Trend Analizi**: Test performansının zaman içindeki değişimi
- ✅ **Hata Takibi**: Belirli tarihlerdeki hataları inceleme
- ✅ **Metadata**: Test süreleri ve detayları

### Rapor Görüntüleme:
```bash
# En son raporu görüntüle
allure serve reports/$(ls reports | tail -1)/$(ls reports/$(ls reports | tail -1) | tail -1)/allure-results

# Belirli tarihteki raporu görüntüle
allure serve reports/2024-08-14/134523/allure-results
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 