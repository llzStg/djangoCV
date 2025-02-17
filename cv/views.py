from django.shortcuts import render

# Create your views here.
def cv_view(request):
    # 这里的数据可以改成你的简历内容
    cv_data = {
        "name": "your name",
        "email": "your.email@example.com",
        "phone": "+1 123 456 7890",
        "summary": "a short self description",
        "experience": [
            {"position": "sde intern", "company": "A", "duration": "2022-now", "description": "java dev"},
            {"position": "sde intern", "company": "B", "duration": "2020-2022", "description": "java dev"}
        ],
        "education": [
            {"degree": "xxx", "school": "nyu", "year": "2022"}
        ],
        "skills": ["Python", "Django", "SQL", "ML"]
    }
    return render(request, "cv/cv_template.html", {"cv": cv_data})
