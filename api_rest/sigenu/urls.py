from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from sigenu import views
from assets import serializers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'employee', views.EmployeeViewSet)
# router.register(r'department', views.DepartmentViewSet)
router.register(r'students', views.StudentAllViewSet)
router.register(r'students_active', views.StudentAllActiveViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'student_type', views.StudentTypeViewSet)
router.register(r'career', views.CareerViewSet)
router.register(r'entry_source', views.EntrySourceViewSet)
router.register(r'course_type', views.CourseTypeViewSet)
router.register(r'scholastic_origin', views.ScholasticOriginViewSet)
router.register(r'politic_org', views.PoliticOrgViewSet)
router.register(r'sex', views.SexViewSet)
router.register(r'town_university', views.TownUniversityViewSet)
router.register(r'marital_status', views.MaritalStatusViewSet)
router.register(r'study_regimen', views.StudyRegimenViewSet)
router.register(r'academic_situation', views.AcademicSituationViewSet)
router.register(r'town_situation', views.TownSituationViewSet)
router.register(r'skin_color', views.SkinColorViewSet)
router.register(r'student_status', views.StudentStatusViewSet)
router.register(r'faculty', views.FacultyViewSet)
router.register(r'orphan', views.OrphanViewSet)



router.get_api_root_view().cls.__name__ = "Raiz del Api Sigenu"

router.get_api_root_view().cls.__doc__ = "{student_active_name_full : http://localhost:port/student_active_name_full/NomBr SegNom} \n" \
                                         "--------------"

urlpatterns = [
    #path('/api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('student_dni/<str:ci>/', views.student_dni),
    path('student_active_dni/<str:ci>/', views.student_active_dni),
    path('student_active_name_full/<str:name_full>/', views.student_active_name_full),
    path('search_active', views.ActivosList.as_view()),
    #path('search_inactive', views.ActivosList.as_view()),#NO IMPLEMENTADO TODAVIA
    #path('search_all', views.ActivosList.as_view()),#NO IMPLEMENTADO TODAVIA

]