# Create your models here.
from django.db import models
from django.db.models import Q
from django.utils import timezone


# Create your models here.
class BreastExaminationValueRecord(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CancerMarkerRecords(models.Model):
    name = models.CharField(max_length=300)
    unit = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cancer Marker Records"

class CancerMarker(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    name = models.ForeignKey(CancerMarkerRecords, on_delete=models.CASCADE, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name.name

class ScocioEconomicStatus(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Socio Economic Status"

class Patient(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    BLOOD_GRoup_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),   
    )
    unique_id = models.CharField(unique=True, max_length=16)
    name = models.CharField(max_length=300, null=False, blank=False)
    phone = models.BigIntegerField(unique=True, help_text="Phone number must be 11 digits")
    email = models.EmailField(null=True, blank=True)
    nid = models.CharField(max_length=25, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True, default='Female')
    blood_group = models.CharField(choices=BLOOD_GRoup_CHOICES, null=True, blank=True, max_length=10)
    area = models.CharField(max_length=300, null=True, blank=True)
    police_station = models.CharField(max_length=300, null=True, blank=True)
    district = models.CharField(max_length=300, null=True, blank=True)
    socio_economic_status = models.ForeignKey(ScocioEconomicStatus, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    passport = models.ImageField(upload_to='photos/', null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email_not_null', condition=~models.Q(email=None)),
            models.UniqueConstraint(fields=['nid'], name='unique_nid_not_null', condition=~models.Q(nid=None)),
        ]

    def __str__(self):
        return self.name
    
class Center(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=300)
    phone = models.BigIntegerField(blank=True, null=True, help_text="Phone number must be 11 digits")
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=300, null=True, blank=True)
    department = models.CharField(max_length=300, null=True, blank=True)
    institution = models.CharField(max_length=300, null=True, blank=True)
    bmdc_number = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DoctorPatient(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor_id} - {self.patient_id}"

class District(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PoliceStations(models.Model):
    name = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Police Stations"
    
class ChemotherapyModalityRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Chemotherapy Modality Records"

class ChemotherapyModalities(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    detail = models.ForeignKey(ChemotherapyModalityRecords, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.detail.name if self.detail else "No Modality"

    class Meta:
        verbose_name_plural = "Chemotherapy Modalities"
    
class ChemotherapyProtocolRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Chemotherapy Protocol Records"

class ChemotherapyProtocol(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    cycle_no = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"Cycle {self.cycle_no} - {self.type}"
    
class ChemotherapyProtocolDetails(models.Model):
    chemotherapy_protocol_id = models.ForeignKey(ChemotherapyProtocol, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.value
    class Meta:
        verbose_name_plural = "Chemotherapy Protocol Details"

class ClockPosition(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    side = models.CharField(max_length=300, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.side} - {self.position}"

class ComorbidityRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Comorbidity Records"

class Comorbidity(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    name = models.ForeignKey(ComorbidityRecords, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name.name if self.name else "No Comorbidity"
    class Meta:
        verbose_name_plural = "Comorbidities"

class ContraceptiveMethodRecords(models.Model):
    contraceptive_methods = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contraceptive_methods
    class Meta:
        verbose_name_plural = "Contraceptive Method Records"

class DiagnosisLaterality(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Laterality"

class Diagnosis(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.detail
    
    class Meta:
        verbose_name_plural = "Diagnosis" 

class DiagnosisDiseaseGroupRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Disease Group Records"

class DiagnosisDiseaseSubGroupRecords(models.Model):
    diagnosis_disease_group = models.ForeignKey(DiagnosisDiseaseGroupRecords, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Disease Sub Group Records"

class DiagnosisGroupRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Group Records"

class ErStatus(models.Model):
    er_status = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.er_status
    
    class Meta:
        verbose_name_plural = "ER Status"

class PrStatus(models.Model):
    pr_status = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pr_status if self.pr_status else "N/A"

    
    class Meta:
        verbose_name_plural = "PR Status"

class Her2Status(models.Model):
    her2_status = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.her2_status
    
    class Meta:
        verbose_name_plural = "HER2 Status"

class Ki67Status(models.Model):
    ki67_status = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ki67_status
    
    class Meta:
        verbose_name_plural = "KI67 Status"

class LuminalCriteria(models.Model):
    results = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.results
    
    class Meta:
        verbose_name_plural = "Luminal Criteria"

class DiagnosisGroupCalculationRecords(models.Model):
    er = models.ForeignKey(ErStatus, on_delete=models.CASCADE, null=True, blank=True)
    pr = models.ForeignKey(PrStatus, on_delete=models.CASCADE, null=True, blank=True)
    her2 = models.ForeignKey(Her2Status, on_delete=models.CASCADE, null=True, blank=True)
    ki67 = models.ForeignKey(Ki67Status, on_delete=models.CASCADE, null=True, blank=True)
    results = models.ForeignKey(LuminalCriteria, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.er} - {self.pr} - {self.her2} - {self.ki67} - {self.results}"
    
    class Meta:
        verbose_name_plural = "Diagnosis Group Calculation Records"

class DiagnosisGroup(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    er = models.ForeignKey(ErStatus, on_delete=models.CASCADE, null=True, blank=True)
    pr = models.ForeignKey(PrStatus, on_delete=models.CASCADE, null=True, blank=True) 
    her2 = models.ForeignKey(Her2Status, on_delete=models.CASCADE, null=True, blank=True)
    ki67 = models.ForeignKey(Ki67Status, on_delete=models.CASCADE, null=True, blank=True)
    result = models.ForeignKey(LuminalCriteria, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.er} - {self.pr} - {self.her2} - {self.ki67} - {self.result}"
    
    class Meta:
        verbose_name_plural = "Diagnosis Groups"

class DiagnosisPrimarySiteRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Primary Site Records"

class DiagnosisMetastaticSiteRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Diagnosis Metastastic Site Records"

class HistopathologiesType(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Histopathologies Type Records"

class HistopathologyRecords(models.Model):
    name = models.CharField(max_length=300)
    type = models.ForeignKey(HistopathologiesType, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Histopathology Records"

class LineOfTreatmentRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Line of Treatment Records"

class MolecularPathologies(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name if self.name else "No Molecular Pathology"
    
    class Meta:
        verbose_name_plural = "Molecular Pathologies"

class PastTreatmentHistories(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.detail
    
    class Meta:
        verbose_name_plural = "Past Treatment Histories"

class MaritalStatusRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Marital Status Records"

class MenstrualCycleRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Menstrual Cycle Records"

class PatientHistory(models.Model):
    BREAST_EXAMINATION_CHOICES = (
        ('Self Examination', 'Self Examination'),
        ('Clinical Examination', 'Clinical Examination'),
        ('Mammogram', 'Mammogram'),
        ('Ultrasound', 'Ultrasound'),
    )
    HISTORY_OF_ALCHOLISM_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    HISTORY_OF_HRT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    RT_TO_CHEST_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    CANCER_HISTORY_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    SMOKING_HISTORY_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    marital_status = models.ForeignKey(MaritalStatusRecords, on_delete=models.CASCADE, null=True, blank=True)
    family_member = models.IntegerField(null=True, blank=True)
    age_of_marriage = models.IntegerField(null=True, blank=True)
    age_of_first_child = models.IntegerField(null=True, blank=True)
    contraceptive_method = models.ForeignKey(ContraceptiveMethodRecords, on_delete=models.CASCADE, null=True, blank=True)
    age_of_menarche = models.IntegerField(null=True, blank=True)
    age_of_menopause = models.IntegerField(null=True, blank=True)
    regular_irregular_menstruation = models.ForeignKey(MenstrualCycleRecords, on_delete=models.CASCADE, null=True, blank=True)
    breast_examination = models.CharField(choices=BREAST_EXAMINATION_CHOICES, max_length=300, null=True, blank=True)
    breast_examination_value = models.ForeignKey(BreastExaminationValueRecord, on_delete=models.CASCADE, null=True, blank=True)
    excercise_per_week = models.IntegerField(null=True, blank=True, help_text="Number of excercise per week in hours")
    dietary_habit = models.CharField(max_length=300, null=True, blank=True)
    height = models.FloatField(null=True, blank=True, help_text="Height in cm")
    weight = models.FloatField(null=True, blank=True, help_text="Weight in kg")
    bmi = models.FloatField(null=True, blank=True, help_text="BMI = weight(kg) / height(m)^2")
    h_o_alcholism = models.CharField(choices=HISTORY_OF_ALCHOLISM_CHOICES, max_length=300, null=True, blank=True)
    h_o_hrt = models.CharField(choices=HISTORY_OF_HRT_CHOICES, max_length=300, null=True, blank=True)
    breast_feeding_duration = models.IntegerField(null=True, blank=True, help_text="Breast feeding duration in months")
    rt_to_chest = models.CharField(choices=RT_TO_CHEST_CHOICES, max_length=300, null=True, blank=True)
    cancer_history = models.CharField(choices=CANCER_HISTORY_CHOICES, max_length=300, null=True, blank=True)
    known_mutation = models.CharField(max_length=300, null=True, blank=True)
    first_diagnosis_date = models.DateField(null=True, blank=True)
    smoking_history = models.CharField(choices=SMOKING_HISTORY_CHOICES, max_length=300, null=True, blank=True)
    smoking_packets_per_year = models.IntegerField(null=True, blank=True, help_text="Number of packets smoked per year")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    def __str__(self):
        return f"Patient History for {self.patient_observation_id}"
    
    class Meta:
        verbose_name_plural = "Patient Histories"

class RadiotherapyScheduleIntentRecords(models.Model):
    value = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name_plural = "Radiotherapy Schedule Intent Records"

class RadiotherapyScheduleRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Radiotherapy Schedule Records"

class RadiotherapySchedules(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    intent = models.ForeignKey(RadiotherapyScheduleIntentRecords, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.intent.value if self.intent else "No Intent"
    
    class Meta:
        verbose_name_plural = "Radiotherapy Schedules"

class RadiotherapyScheduleDetails(models.Model):
    radiotherapy_schedule_id = models.ForeignKey(RadiotherapySchedules, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name_plural = "Radiotherapy Schedule Details"
    
class SurgeryModalityRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Surgery Modality Records"
    
class Surgeries(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    surgery_date = models.DateField(null=True, blank=True)
    modality = models.ForeignKey(SurgeryModalityRecords, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.surgery_date} - {self.modality}"
    
    class Meta:
        verbose_name_plural = "Surgeries"

class IHCRecords(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "IHC Records"

class IHCResults(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC Results"

class IHC_ER(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-ER"

class IHC_PR(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-PR"

class IHC_HER2(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-HER2"

class IHC_FISH(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-FISH"
        
class IHC_Synaptophysin(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-Synaptophysin"
        
class IHC_Chromogranin(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-Chromogranin"
        
class IHC_GATA(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-GATA"

class IHC_Others(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IHC-Others"

class IHC(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    ER = models.ForeignKey(IHC_ER, on_delete=models.CASCADE, null=True, blank=True)
    PR = models.ForeignKey(IHC_PR, on_delete=models.CASCADE, null=True, blank=True)
    HER2 = models.ForeignKey(IHC_HER2, on_delete=models.CASCADE, null=True, blank=True)
    FISH = models.ForeignKey(IHC_FISH, on_delete=models.CASCADE, null=True, blank=True)
    Synaptophysin = models.ForeignKey(IHC_Synaptophysin, on_delete=models.CASCADE, null=True, blank=True)
    Chromogranin = models.ForeignKey(IHC_Chromogranin, on_delete=models.CASCADE, null=True, blank=True)
    GATA = models.ForeignKey(IHC_GATA, on_delete=models.CASCADE, null=True, blank=True)
    others = models.ForeignKey(IHC_Others, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ER} - {self.PR} - {self.HER2} - {self.FISH}"

    class Meta:
        verbose_name_plural = "IHC"

class Path_lvsi(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Path LVSI"

class Path_Pni(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Path PNI"
    
class Path_Margin(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Path Margin"

class Path_Ki67(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Path Ki67"

class StagingPathologicalsDetails(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    lvsi = models.ForeignKey(Path_lvsi, on_delete=models.CASCADE, null=True, blank=True)
    pni = models.ForeignKey(Path_Pni, on_delete=models.CASCADE, null=True, blank=True)
    margin = models.ForeignKey(Path_Margin, on_delete=models.CASCADE, null=True, blank=True)
    ki67 = models.ForeignKey(Path_Ki67, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.lvsi} - {self.pni} - {self.margin} - {self.ki67}"

    class Meta:
        verbose_name_plural = "Staging Pathologicals Details"
    
class TumourGrade(models.Model):
    name = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) if self.name is not None else "N/A"

    class Meta:
        verbose_name_plural = "Tumour Grade"

class DiseaseProgressionStatus(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disease Progression Status"

class SurvivalStatus(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Survival Status"

class PFSStatus(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    status = models.ForeignKey(DiseaseProgressionStatus, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.status} - {self.date}"

    class Meta:
        verbose_name_plural = "PFS Status"

class OSStatus(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    status = models.ForeignKey(SurvivalStatus, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.status} - {self.date}"

    class Meta:
        verbose_name_plural = "OS Status"

#---------------------------------------- Response Rates Models STARTS HERE ----------------------------------------#

class ResponseRateType(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Response Rate Types"

class ClinicalResponseRateTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical Response Rate Target Lesions"
    
class PathologicalResponseRateTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological Response Rate Target Lesions"
    
class RadiologicalResponseRateTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Radiological Response Rate Target Lesions"

class ClinicalResponseRateNonTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical Response Rate Non-Target Lesions"

class PathologicalResponseRateNonTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological Response Rate Non-Target Lesions"

class RadiologicalResponseRateNonTargetLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Rdiological Response Rate Non-Target Lesions"

class ClinicalResponseRateNewLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical Response Rate New Lesions"

class PathologicalResponseRateNewLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological Response Rate New Lesions"

class RadiologicalResponseRateNewLesion(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Radiological Response Rate New Lesions"

class ClinicalResponseRateResult(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical Response Rate Results"

class PathologicalResponseRateResult(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological Response Rate Results"

class RadiologicalResponseRateResult(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Radiological Response Rate Results"
    
class ClinicalResponseRateCalculationRecords(models.Model):
    target_lesion = models.ForeignKey(ClinicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_response_rate_target_lesion")
    non_target_lesion = models.ForeignKey(ClinicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_response_rate_non_target_lesion")
    new_lesion = models.ForeignKey(ClinicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_response_rate_new_lesion")
    result = models.ForeignKey(ClinicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_response_rate_result")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.target_lesion} - {self.non_target_lesion} - {self.new_lesion} - {self.result}"
    
    class Meta:
        verbose_name_plural = "Clinical Response Rate Calculation Records"

class PathologicalResponseRateCalculationRecords(models.Model):
    target_lesion = models.ForeignKey(PathologicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_response_rate_target_lesion")
    non_target_lesion = models.ForeignKey(PathologicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_response_rate_non_target_lesion")
    new_lesion = models.ForeignKey(PathologicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_response_rate_new_lesion")
    result = models.ForeignKey(PathologicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_response_rate_result")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.target_lesion} - {self.non_target_lesion} - {self.new_lesion} - {self.result}"
    
    class Meta:
        verbose_name_plural = "Pathological Response Rate Calculation Records"

class RadiologicalResponseRateCalculationRecords(models.Model):
    target_lesion = models.ForeignKey(RadiologicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_response_rate_target_lesion")
    non_target_lesion = models.ForeignKey(RadiologicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_response_rate_non_target_lesion")
    new_lesion = models.ForeignKey(RadiologicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_response_rate_new_lesion")
    result = models.ForeignKey(RadiologicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_response_rate_result")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.target_lesion} - {self.non_target_lesion} - {self.new_lesion} - {self.result}"
    
    class Meta:
        verbose_name_plural = "Radiological Response Rate Calculation Records"

#---------------------------------------- Response Rate Models END HERE ----------------------------------------#

#---------------------------------------- TNM Staging STARTS HERE ----------------------------------------#

class ClinicalTNMStagingT(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical TNM Staging-T"
    
class ClinicalTNMStagingN(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical TNM Staging-N"
    
class ClinicalTNMStagingM(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical TNM Staging-M"
    
class ClinicalTNMStagingResult(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clinical TNM Staging Results"

class ClinicalTNMStagingCalculationRecords(models.Model):
    t = models.ForeignKey(ClinicalTNMStagingT, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_tnm_staging_t")
    n = models.ForeignKey(ClinicalTNMStagingN, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_tnm_staging_n")
    m = models.ForeignKey(ClinicalTNMStagingM, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_tnm_staging_m")
    result = models.ForeignKey(ClinicalTNMStagingResult, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_tnm_staging_result")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.t or '-'} - {self.n or '-'} - {self.m or '-'} - {self.result or '-'}"

    
    class Meta:
        verbose_name_plural = "Clinical TNM Staging Calculation Records"

class StagingClinicals(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    t = models.ForeignKey(ClinicalTNMStagingT, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_t_staging")
    n = models.ForeignKey(ClinicalTNMStagingN, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_n_staging")
    m = models.ForeignKey(ClinicalTNMStagingM, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_m_staging")
    result = models.ForeignKey(ClinicalTNMStagingResult, on_delete=models.CASCADE, null=True, blank=True, related_name="clinical_result_staging")
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.t} - {self.n} - {self.m} - {self.result} - {self.date}"
    
    class Meta:
        verbose_name_plural = "Staging Clinicals"

#---------------------------------------- Pathological Staging STARTS HERE ----------------------------------------#

class PathologicalTNMStagingT(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological TNM Staging-T"
    
class PathologicalTNMStagingN(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological TNM Staging-N"
    
class PathologicalTNMStagingM(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological TNM Staging-M"
    
class PathologicalTNMStagingResult(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pathological TNM Staging Results"

class PathologicalTNMStagingCalculationRecords(models.Model):
    t = models.ForeignKey(PathologicalTNMStagingT, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_tnm_staging_t")
    n = models.ForeignKey(PathologicalTNMStagingN, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_tnm_staging_n")
    m = models.ForeignKey(PathologicalTNMStagingM, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_tnm_staging_m")
    result = models.ForeignKey(PathologicalTNMStagingResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_tnm_staging_result")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.t or '-'} - {self.n or '-'} - {self.m or '-'} - {self.result or '-'}"

    
    class Meta:
        verbose_name_plural = "Pathological TNM Staging Calculation Records"


class StagingPathologicals(models.Model):
    patient_observation_id = models.ForeignKey('PatientObservation', on_delete=models.CASCADE)
    t = models.ForeignKey(PathologicalTNMStagingT, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_t_staging")
    n = models.ForeignKey(PathologicalTNMStagingN, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_n_staging")
    m = models.ForeignKey(PathologicalTNMStagingM, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_m_staging")
    result = models.ForeignKey(PathologicalTNMStagingResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_result_staging")
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.t} - {self.n} - {self.m} - {self.result} - {self.date}"
    
    class Meta:
        verbose_name_plural = "Staging Pathologicals"

#---------------------------------------- Pathological Staging ENDS HERE ----------------------------------------#

#---------------------------------------- TNM Staging ENDS HERE ----------------------------------------#



#---------------------------------------- Patient Observation Model STARTS HERE ----------------------------------------#

class PatientObservation(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="observations", null=True, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True, related_name="observations")
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True, related_name="observations")
    time = models.DateTimeField(default=timezone.now)
    registration_number = models.CharField(max_length=300, null=True, blank=True)
    laterality = models.CharField(max_length=300, null=True, blank=True)
    grade = models.ForeignKey(TumourGrade, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    current_chemo_protocol = models.TextField(null=True, blank=True)
    chemo_starting_date = models.DateField(null=True, blank=True)
    chemo_cycle_no = models.IntegerField(null=True, blank=True)
    chemo_detail = models.TextField(null=True, blank=True)
    disease_progression_status = models.ForeignKey(DiseaseProgressionStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    disease_progression_status_date = models.DateField(null=True, blank=True)
    pfs = models.FloatField(null=True, blank=True)
    survival_status = models.ForeignKey(SurvivalStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    survival_status_date = models.DateField(null=True, blank=True)
    overall_survival = models.FloatField(null=True, blank=True)
    line_of_treatment = models.ForeignKey(LineOfTreatmentRecords, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    diagnosis_disease_group = models.ForeignKey(DiagnosisDiseaseGroupRecords, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    diagnosis_subgroup = models.ForeignKey(DiagnosisDiseaseSubGroupRecords, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    diagnosis_primary_site = models.ForeignKey(DiagnosisPrimarySiteRecords, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_observations")
    diagnosis_laterility = models.ForeignKey(DiagnosisLaterality, on_delete=models.CASCADE, null=True, blank=True, related_name="laterality_observations")
    clinical_response_rate_target_lasion = models.ForeignKey(ClinicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_target_observations")
    clinical_response_rate_non_target_lasion = models.ForeignKey(ClinicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_non_target_observations")
    clinical_response_rate_new_lasion = models.ForeignKey(ClinicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_new_observations")
    clinical_response_rate_result = models.ForeignKey(ClinicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="clinical_result_observations")
    clinical_response_rate_date = models.DateField(null=True, blank=True)
    radiological_response_rate_target_lasion = models.ForeignKey(RadiologicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_target_observations")
    radiological_response_rate_non_target_lasion = models.ForeignKey(RadiologicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_non_target_observations")
    radiological_response_rate_new_lasion = models.ForeignKey(RadiologicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_new_observations")
    radiological_response_rate_result = models.ForeignKey(RadiologicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="radiological_result_observations")
    radiological_response_rate_date = models.DateField(null=True, blank=True)
    pathological_response_rate_target_lasion = models.ForeignKey(PathologicalResponseRateTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_target_observations")
    pathological_response_rate_non_target_lasion = models.ForeignKey(PathologicalResponseRateNonTargetLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_non_target_observations")
    pathological_response_rate_new_lasion = models.ForeignKey(PathologicalResponseRateNewLesion, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_new_observations")
    pathological_response_rate_result = models.ForeignKey(PathologicalResponseRateResult, on_delete=models.SET_NULL, null=True, blank=True, related_name="pathological_result_observations")
    pathological_response_rate_date = models.DateField(null=True, blank=True)
    cancer_type = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" {self.id} - {self.patient_id}"

    class Meta:
        verbose_name_plural = "Patient Observations"

#-------------------------------------------------------- Patient Observations End ---------------------------------------------------------------------------------#
# -------------------------------------------------------- All Data Models START ---------------------------------------------------------------------------------#
from django.db.models.signals import post_save
from django.dispatch import receiver

class AllData(models.Model):
    patient_observation = models.OneToOneField('PatientObservation', on_delete=models.CASCADE)

    cancer_marker = models.ForeignKey('CancerMarker', on_delete=models.SET_NULL, null=True, blank=True)
    chemotherapy_modalities = models.ForeignKey('ChemotherapyModalities', on_delete=models.SET_NULL, null=True, blank=True)
    chemotherapy_protocol = models.ForeignKey('ChemotherapyProtocol', on_delete=models.SET_NULL, null=True, blank=True)
    clock_position = models.ForeignKey('ClockPosition', on_delete=models.SET_NULL, null=True, blank=True)
    comorbidity = models.ForeignKey('Comorbidity', on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.ForeignKey('Diagnosis', on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis_group = models.ForeignKey('DiagnosisGroup', on_delete=models.SET_NULL, null=True, blank=True)
    molecular_pathologies = models.ForeignKey('MolecularPathologies', on_delete=models.SET_NULL, null=True, blank=True)
    past_treatment_histories = models.ForeignKey('PastTreatmentHistories', on_delete=models.SET_NULL, null=True, blank=True)
    patient_history = models.ForeignKey('PatientHistory', on_delete=models.SET_NULL, null=True, blank=True)
    radiotherapy_schedules = models.ForeignKey('RadiotherapySchedules', on_delete=models.SET_NULL, null=True, blank=True)
    surgeries = models.ForeignKey('Surgeries', on_delete=models.SET_NULL, null=True, blank=True)
    ihc = models.ForeignKey('IHC', on_delete=models.SET_NULL, null=True, blank=True)
    staging_pathologicals_details = models.ForeignKey('StagingPathologicalsDetails', on_delete=models.SET_NULL, null=True, blank=True)
    pfs_status = models.ForeignKey('PFSStatus', on_delete=models.SET_NULL, null=True, blank=True)
    os_status = models.ForeignKey('OSStatus', on_delete=models.SET_NULL, null=True, blank=True)
    staging_clinicals = models.ForeignKey('StagingClinicals', on_delete=models.SET_NULL, null=True, blank=True)
    staging_pathologicals = models.ForeignKey('StagingPathologicals', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"AllData for PatientObservation {self.patient_observation_id}"



