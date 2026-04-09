from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from doctors.models import Doctor
from appointment.models import Appointment 
from django.conf import settings
import google.generativeai as genai
from markdown_it import MarkdownIt

# ✅ Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)


# ================= DASHBOARD =================
@login_required(login_url='login')
def dashboard_home(request):   # ✅ FIXED
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, "dashboard.html", {
        'patient_list': patients,
        'doctor_list': doctors
    })


# ================= APPOINTMENT =================
@login_required(login_url='login')
def appointment_list(request):
    return render(request, "appointment.html")


# ================= AI CHATBOT =================
@login_required
def hospital_ai(request):
    answer = None
    error_message = None
   
    if request.method == 'POST':
        try:
            user_query = request.POST.get('query')
           
            if not user_query or user_query.strip() == '':
                error_message = "Please enter a question."
            else:
                # Configure the API key
                genai.configure(api_key=settings.GEMINI_API_KEY)
               
                # Get database data
                doctors = Doctor.objects.all()
                appointments = Appointment.objects.all()
                patients = Patient.objects.all()
 
                final_query = f'''
            You are the AI chatbot inside a website called medhaHMS
            You responsibility is to answer questions about
            medhaHMS data. Anything part from this, you are not allowed to
            answer. Below is the doctor data you need to know.
            {doctors} and below are patients {patients}
            and below are appointments {appointments}
 
            answer below:
            {user_query}
            '''
               
                # Generate response using Gemini API
                model = genai.GenerativeModel("gemini-3-flash-preview")
                response = model.generate_content(final_query)
               
                # Convert markdown to HTML
                md = MarkdownIt()
                answer = md.render(response.text)
               
        except Exception as e:
            error_message = f"Error connecting to AI service: {str(e)}"
            print(f"Gemini API Error: {str(e)}")
 
    return render(request, 'G_ai.html', {'answer': answer, 'error_message': error_message})
 