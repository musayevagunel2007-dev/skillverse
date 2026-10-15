from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Peşə istiqamətləri və onların detallı tələbləri, resursları, müsahibə sualları
ROLES_DATA = {
    "backend": {
        "title": "Backend Developer",
        "description": "Server tərəfi məntiqinin, verilənlər bazalarının və API-lərin qurulması.",
        "skills": ["Python", "SQL", "Flask", "Docker", "Git", "Linux"],
        "project": "RESTful API və PostgreSQL bazası ilə e-ticarət backend sistemi qur.",
        "project_details": {
            "title": "E-Ticarət REST API Platforması",
            "stack": "Python, Flask, PostgreSQL, Docker, Git",
            "steps": [
                "Database arxitekturasını (Users, Products, Orders) layihələndir.",
                "JWT Authentication ilə istifadəçi giriş/qeydiyyat API-lərini yaz.",
                "Məhsul axtarışı və səbət (Cart) məntiqini tətbiq et.",
                "Docker konteynerləşdirilməsini et və GitHub-a yüklə."
            ]
        },
        "resources": [
            {"title": "Python Official Docs", "url": "https://docs.python.org/3/"},
            {"title": "SQL Tutorial (W3Schools)", "url": "https://www.w3schools.com/sql/"},
            {"title": "Flask Documentation", "url": "https://flask.palletsprojects.com/"}
        ],
        "interview_tips": [
            "REST API prinsipləri (GET, POST, PUT, DELETE) haqqında aydın danışmağa hazırlaş.",
            "SQL sorgularının optimallaşdırılması və JOIN növlərini izah etməyi məşq et.",
            "DATABASE indexing və ACID xassələri haqqında suallara bax."
        ]
    },
    "frontend": {
        "title": "Frontend Developer",
        "description": "İstifadəçi interfeyslərinin və veb təcrübəsinin vizual olaraq hazırlanması.",
        "skills": ["HTML/CSS", "JavaScript", "React", "Git"],
        "project": "React və Tailwind CSS istifadə edərək interaktiv Tapşırıq İdarəetmə Paneli (Dashboard) yaz.",
        "project_details": {
            "title": "Interaktiv Tapşırıq İdarəetmə Paneli",
            "stack": "React, Tailwind CSS, JavaScript, Git",
            "steps": [
                "UI komponentləri (Sidebar, Header, Task Cards) düzəlt.",
                "State Management (React Context / Redux) ilə tapşırıq əlavə etmə/silmə funksiyası yaz.",
                "Dark/Light rejimi keçidini əlavə et."
            ]
        },
        "resources": [
            {"title": "MDN Web Docs (JS)", "url": "https://developer.mozilla.org/"},
            {"title": "React Documentation", "url": "https://react.dev/"}
        ],
        "interview_tips": [
            "JavaScript Closure, Event Loop və Async/Await mövzularını dərin öyrən.",
            "React Virtual DOM və State Management məntiqini izah edə bilməlisən."
        ]
    },
    "fullstack": {
        "title": "Full Stack Developer",
        "description": "Həm Frontend, həm də Backend hissələrinin tam hazırlanması.",
        "skills": ["Python", "SQL", "Flask", "HTML/CSS", "JavaScript", "React", "Git", "Docker"],
        "project": "Full-stack bloq platforması hazırlayaraq Docker ilə konteynerləşdir.",
        "project_details": {
            "title": "Full-Stack Bloq Platforması",
            "stack": "Python, Flask, React, SQL, Docker",
            "steps": [
                "Flask ilə autentifikasiya və post idarəetmə API-lərini qur.",
                "React ilə interaktiv frontend interfeysini hazırla.",
                "Frontend və Backend-i bir-birinə bağlayıb Docker ilə işə sal."
            ]
        },
        "resources": [
            {"title": "Full Stack Open Course", "url": "https://fullstackopen.com/en/"},
            {"title": "Docker Documentation", "url": "https://docs.docker.com/"}
        ],
        "interview_tips": [
            "Front-end və Back-end arasında təhlükəsizlik (CORS, JWT Authentication) məsələlərini cavablandırmağa hazırlaş.",
            "Sistem arxitekturası (MVC pattern) haqqında biliklərini təkrarla."
        ]
    },
    "data_analyst": {
        "title": "Data Analyst / Scientist",
        "description": "Məlumatların toplanması, təmizlənməsi, təhlili və vizuallaşdırılması.",
        "skills": ["Python", "SQL", "Pandas/NumPy", "PowerBI/Tableau", "Git"],
        "project": "Müştəri itkisi (Churn Rate) məlumatlarını Pandas ilə təhlil et və PowerBI dashboard-u yarat.",
        "project_details": {
            "title": "Müştəri İtkisi (Churn Rate) Analitika Paneli",
            "stack": "Python, Pandas, NumPy, PowerBI",
            "steps": [
                "Dataset-i təmizlə və əskik məlumatları bərpa et.",
                "Pandas ilə statistik təhlillər aparıb vizual qrafiklər qur.",
                "Nəticələri PowerBI üzərində interaktiv dashboard-a çevir."
            ]
        },
        "resources": [
            {"title": "Kaggle Datasets & Courses", "url": "https://www.kaggle.com/"},
            {"title": "Pandas User Guide", "url": "https://pandas.pydata.org/docs/"}
        ],
        "interview_tips": [
            "Groupby, Merge və missing value (əskik məlumatlar) təmizləmə metodlarını dəqiq izah et.",
            "Biznes metrikaları (ROI, KPI) və Vizualizasiya seçimlərini əsaslandırmağı bacar."
        ]
    },
    "cybersecurity": {
        "title": "Kibertəhlükəsizlik Mütəxəssisi",
        "description": "Şəbəkə sistemlərinin və məlumatların kiberhücumalardan qorunması.",
        "skills": ["Python", "Networking", "Linux", "Git", "SQL"],
        "project": "Python ilə şəbəkə portlarını skan edən (Port Scanner) alət yaz.",
        "project_details": {
            "title": "Avtomatlaşdırılmış Port Scanner və Zəiflik Təhlili Aləti",
            "stack": "Python, Socket Library, Nmap, Linux",
            "steps": [
                "Python `socket` kitabxanası ilə IP və Port bağlantısı quran skript yaz.",
                "Çoxlu portları eyni anda skan etmək üçün Multithreading tətbiq et.",
                "Açıq portlar üzərində işləyən servisləri tapıb hesabat şəklində fayla yaz."
            ]
        },
        "resources": [
            {"title": "TryHackMe Learning Paths", "url": "https://tryhackme.com/"},
            {"title": "Cybrary Security Courses", "url": "https://www.cybrary.it/"}
        ],
        "interview_tips": [
            "OSI modeli və TCP/IP protokolları haqqında detallı suallara hazırlaş.",
            "OWASP Top 10 zəiflikləri (SQL Injection, XSS və s.) izah edə bilməlisən."
        ]
    },
    "ai_ml": {
        "title": "Süni İntellekt / ML Mühendisi",
        "description": "Maşın öyrənməsi və dərin öyrənmə modellərinin qurulması.",
        "skills": ["Python", "Pandas/NumPy", "PyTorch/TensorFlow", "SQL", "Git"],
        "project": "Şəkilləri təsnifləndirən CNN (Convolutional Neural Network) modeli qur.",
        "project_details": {
            "title": "CNN ilə Təsvirlərin Təsnifləndirilməsi Modeli",
            "stack": "Python, PyTorch/TensorFlow, NumPy",
            "steps": [
                "Şəkil datasetini yüklə və pre-processing et.",
                "CNN arxitekturasını qur.",
                "Modeli öyrət və dəqiqlik qrafiklərini çıxar."
            ]
        },
        "resources": [
            {"title": "Fast.ai Courses", "url": "https://www.fast.ai/"},
            {"title": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"}
        ],
        "interview_tips": [
            "Overfitting, Underfitting və Requlyarizasiya anlayışlarını izah etməyi öyrən.",
            "Model dəyərləndirmə metrikaları (Precision, Recall, F1-Score) üzrə suallara hazırlaş."
        ]
    },
    "devops": {
        "title": "DevOps / Bulud Mühendisi",
        "description": "Proqram təminatının avtomatlaşdırılmış yerləşdirilməsi və infrastruktur idarəetməsi.",
        "skills": ["Linux", "Docker", "Kubernetes", "Git", "Python"],
        "project": "CI/CD pipeline quraraq tətbiqi avtomatik Kubernetes klasterinə deploy et.",
        "project_details": {
            "title": "Avtomatlaşdırılmış CI/CD Pipeline",
            "stack": "Docker, Kubernetes, GitHub Actions, Linux",
            "steps": [
                "Tətbiqi Docker image halına gətir.",
                "GitHub Actions ilə avtomatik build pipeline-ı yaz.",
                "Kubernetes manifest faylları ilə klasterə deploy et."
            ]
        },
        "resources": [
            {"title": "Roadmap.sh DevOps", "url": "https://roadmap.sh/devops"},
            {"title": "Kubernetes Docs", "url": "https://kubernetes.io/docs/"}
        ],
        "interview_tips": [
            "CI/CD proseslərini və Docker image optimallaşdırılmasını izah et.",
            "Linux əmrləri və Bash skript yazma bacarıqlarını nümayiş etdir."
        ]
    },
    "mobile": {
        "title": "Mobil Tətbiq Tərtibatçısı",
        "description": "iOS və Android platformaları üçün mobil tətbiqlərin hazırlanması.",
        "skills": ["JavaScript", "React", "Git"],
        "project": "React Native ilə canlı hava durumu göstərən mobil tətbiq yaz.",
        "project_details": {
            "title": "Canlı Hava Durumu Mobil Tətbiqi",
            "stack": "React Native, JavaScript, OpenWeather API",
            "steps": [
                "Mobil interfeysi və geolokasiya alətini qur.",
                "OpenWeather API-dən canlı məlumatları çək.",
                "Məkan axtarışı funksiyasını əlavə et."
            ]
        },
        "resources": [
            {"title": "React Native Docs", "url": "https://reactnative.dev/"}
        ],
        "interview_tips": [
            "Mobil tətbiq həyat dövrü (Lifecycle) və State idarəolunmasını məşq et.",
            "Native və Cross-Platform karkasların fərqlərini bilməlisən."
        ]
    },
    "embedded": {
        "title": "Quraşdırılmış Sistemlər (Embedded)",
        "description": "Mikrokontrollerlər və aparat təminatı səviyyəsində proqramlaşdırma.",
        "skills": ["C++", "Linux", "Git"],
        "project": "C++ ilə Mikrokontroller üzərində sensor məlumatlarını oxuyan sistem yaz.",
        "project_details": {
            "title": "Mikrokontrollerlə Sensor Monitorinq Sistemi",
            "stack": "C++, Linux, Arduino/ESP32",
            "steps": [
                "Mikrokontrollerə sensorları qoşmaq üçün C++ driveri yaz.",
                "I2C/SPI protokolları ilə verilənləri oxu.",
                "Məlumatları serial port üzərindən ekrana çıxar."
            ]
        },
        "resources": [
            {"title": "Embedded.fm Resources", "url": "https://embedded.fm/"}
        ],
        "interview_tips": [
            "Yaddaş idarəetməsi (Pointers, Memory Leaks) və RTOS haqqında cavab verə bilməlisən."
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', roles=ROLES_DATA)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_role_key = data.get('role')
    user_skills = set(data.get('skills', []))

    if not selected_role_key or selected_role_key not in ROLES_DATA:
        return jsonify({"error": "Keçərsiz peşə seçimi"}), 400

    role_info = ROLES_DATA[selected_role_key]
    required_skills = set(role_info["skills"])
    
    # Uyğunluq dərəcəsinin hesablanması
    matched_skills = list(user_skills.intersection(required_skills))
    missing_skills = list(required_skills - user_skills)
    
    total_required = len(required_skills)
    match_percentage = int((len(matched_skills) / total_required) * 100) if total_required > 0 else 0

    # Status Mətnləri
    if match_percentage >= 80:
        status_tag = "🚀 İşə Qəbul Üçün Hazırsan!"
        status_color = "#10B981"
    elif match_percentage >= 50:
        status_tag = "⚡ Yaxşı Nəticədir, Biraz da Təkmilləşdir"
        status_color = "#F59E0B"
    else:
        status_tag = "📖 Ciddi Çalışmaq Lazımdır"
        status_color = "#EF4444"

    # Vaxt Hesablanması (Hər çatışmayan bacarıq üçün orta hesabla 2 həftə)
    weeks_needed = len(missing_skills) * 2
    estimated_time = f"{weeks_needed} Həftə (~{weeks_needed * 7} Gün)" if weeks_needed > 0 else "Hazırsınız! (0 Gün)"

    return jsonify({
        "role_title": role_info["title"],
        "description": role_info["description"],
        "match_percentage": match_percentage,
        "status_tag": status_tag,
        "status_color": status_color,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "project_idea": role_info["project"],
        "project_details": role_info.get("project_details", {}),
        "estimated_time": estimated_time,
        "resources": role_info["resources"],
        "interview_tips": role_info["interview_tips"]
    })

# Yeni Əlavə Olunan CV Generator Route-u
@app.route('/generate_cv', methods=['POST'])
def generate_cv():
    data = request.json
    name = data.get('name', '')
    contact = data.get('contact', '')
    target_role = data.get('target_role', '')
    education = data.get('education', '')
    skills = data.get('skills', '')
    experience = data.get('experience', '')

    return jsonify({
        "status": "success",
        "cv_data": {
            "name": name,
            "contact": contact,
            "target_role": target_role,
            "education": education,
            "skills": [s.strip() for s in skills.split(',') if s.strip()],
            "experience": experience
        }
    })

if __name__ == '__main__':
    app.run(debug=True)