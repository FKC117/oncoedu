from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import CharWidget

# Register your models here.


@admin.register(BreastExaminationValueRecord)
class BreastExaminationValueRecordAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(CancerMarkerRecords)
class CancerMarkerRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'unit', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    list_per_page = 50
@admin.register(CancerMarker)
class CancerMarkerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'name', 'value', 'unit', 'date', 'created_at', 'updated_at')
    search_fields = ('name__name',)
    list_per_page = 50
    list_display_links = ('id', 'name', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('id', 'unique_id', 'name', 'phone', 'email', 'nid', 'created_at', 'updated_at')
    search_fields = ('unique_id', 'name', 'phone', 'email', 'nid')
    list_per_page = 50
    list_display_links = ('id', 'unique_id', 'name')

@admin.register(ScocioEconomicStatus)
class SocioEconomicStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Center)
class CenterAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'designation', 'department', 'institution', 'created_at', 'updated_at')
    search_fields = ('name', 'phone', 'email', 'designation', 'department', 'institution')
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(DoctorPatient)
class DoctorPatientAdmin(ImportExportModelAdmin):
    list_display = ('id', 'doctor_id', 'patient_id', 'created_at', 'updated_at')
    search_fields = ('doctor_id__name', 'patient_id__name')
    list_per_page = 50
    list_display_links = ('id', 'doctor_id', 'patient_id')
@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PoliceStations)
class PoliceStationsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'district', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name', 'district')

@admin.register(ChemotherapyModalityRecords)
class ChemotherapyModalityRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ChemotherapyModalities)
class ChemotherapyModalitiesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'detail', 'created_at', 'updated_at')
    search_fields = ('detail__name',)
    list_per_page = 50
    list_display_links = ('id', 'detail', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(ChemotherapyProtocolRecords)
class ChemotherapyProtocolRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ChemotherapyProtocol)
class ChemotherapyProtocolAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'cycle_no', 'type', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id',)
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(ChemotherapyProtocolDetails)
class ChemotherapyProtocolDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'chemotherapy_protocol_id', 'value', 'created_at', 'updated_at')
    search_fields = ('chemotherapy_protocol_id', 'patient_observation_id')
    list_per_page = 50
    list_display_links = ('id', 'chemotherapy_protocol_id')

@admin.register(ClockPosition)
class ClockPositionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'side', 'position', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'side')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(ComorbidityRecords)
class ComorbidityRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Comorbidity)
class ComorbidityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'get_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'patient_observation_id', 'get_name')
    search_fields = ('name__name',)
    list_per_page = 50
    autocomplete_fields = ('patient_observation_id',)

    def get_name(self, obj):
        if obj.name:
            return obj.name.name
        return "❌ No Name"
    get_name.short_description = "Comorbidity Name"

@admin.register(ContraceptiveMethodRecords)
class contraceptiveMethodRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'contraceptive_methods', 'created_at', 'updated_at')
    search_fields = ('contraceptive_methods',)
    list_per_page = 50
    list_display_links = ('id', 'contraceptive_methods')

@admin.register(Diagnosis)
class DiagnosisAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'detail', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'detail')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'detail')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(DiagnosisLaterality)
class DiagnosisLateralityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(DiagnosisDiseaseGroupRecords)
class DiagnosisDiseaseGroupRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(DiagnosisDiseaseSubGroupRecords)
class DiagnosisDiseaseSubGroupRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'diagnosis_disease_group', 'name', 'created_at', 'updated_at') # Changed
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'diagnosis_disease_group', 'name')
    #Add this function to display name
    def diagnosis_disease_group_records_name(self, obj):
        return obj.diagnosis_disease_group.name if obj.diagnosis_disease_group else None
    diagnosis_disease_group_records_name.short_description = 'Diagnosis Disease Group Name'

@admin.register(ErStatus)
class ErStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'er_status', 'created_at', 'updated_at')
    search_fields = ('er_status',)
    list_per_page = 50
    list_display_links = ('id', 'er_status')
@admin.register(PrStatus)
class PrStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'pr_status', 'created_at', 'updated_at')
    search_fields = ('pr_status',)
    list_per_page = 50
    list_display_links = ('id', 'pr_status')
@admin.register(Her2Status)
class Her2StatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'her2_status', 'created_at', 'updated_at')
    search_fields = ('her2_status',)
    list_per_page = 50
    list_display_links = ('id', 'her2_status')
@admin.register(Ki67Status)
class Ki67StatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ki67_status', 'created_at', 'updated_at')
    search_fields = ('ki67_status',)
    list_per_page = 50
    list_display_links = ('id', 'ki67_status')
@admin.register(LuminalCriteria)
class LuminalCriteriaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'results', 'created_at', 'updated_at')
    search_fields = ('results',)
    list_per_page = 50
    list_display_links = ('id', 'results')
@admin.register(DiagnosisGroupCalculationRecords)
class DiagnosisGroupCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'er', 'pr', 'her2', 'ki67', 'results', 'created_at', 'updated_at')
    search_fields = ('results',)
    list_per_page = 50
    list_display_links = ('id', 'results')

@admin.register(DiagnosisGroupRecords)
class DiagnosisGroupRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')
        
@admin.register(DiagnosisGroup)
class DiagnosisGroupAdmin(ImportExportModelAdmin):
    list_display = ('patient_observation_id', 'er', 'pr', 'her2', 'ki67', 'result', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id',)
    list_filter = ('created_at', 'updated_at')
    list_per_page = 50
    list_display_links = ('patient_observation_id',)
    autocomplete_fields = ('patient_observation_id',)
    
@admin.register(DiagnosisPrimarySiteRecords)
class DiagnosisPrimarySiteRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')
@admin.register(DiagnosisMetastaticSiteRecords)
class DiagnosisMetastaticSiteRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(HistopathologiesType)
class HistopathologiesTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(HistopathologyRecords)
class HistopathologyRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'type', 'created_at', 'updated_at')
    search_fields = ('name', 'type')
    list_per_page = 50
    list_display_links = ('id', 'name', 'type')

@admin.register(LineOfTreatmentRecords)
class LineOfTreatmentRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(MolecularPathologies)
class MolecularPathologiesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'name', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'name')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'name')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(PastTreatmentHistories)
class PastTreatmentHistoriesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'detail', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'detail')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'detail')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(MaritalStatusRecords)
class MaritalStatusRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')
@admin.register(MenstrualCycleRecords)
class MenstrualCycleRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PatientHistory)
class PatientHistoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'marital_status', 'bmi', 'first_diagnosis_date')
    search_fields = ('patient_observation_id',)
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(RadiotherapyScheduleIntentRecords)
class RadiotherapyScheduleIntentRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'value', 'created_at', 'updated_at')
    search_fields = ('value',)
    list_per_page = 50

@admin.register(RadiotherapyScheduleRecords)
class RadiotherapyScheduleRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(RadiotherapySchedules)
class RadiotherapySchedulesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'intent', 'start_date', 'end_date')
    search_fields = ('patient_observation_id', 'intent')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'intent')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(RadiotherapyScheduleDetails)
class RadiotherapyScheduleDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'radiotherapy_schedule_id', 'value', 'created_at', 'updated_at')
    search_fields = ('radiotherapy_schedule_id',)
    list_per_page = 50
    list_display_links = ('id', 'radiotherapy_schedule_id')
    

@admin.register(ResponseRateType)
class ResponseRateTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalResponseRateTargetLesion)
class ClinicalResponseRateTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalResponseRateTargetLesion)
class PathologicalResponseRateTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(RadiologicalResponseRateTargetLesion)
class RadiologicalResponseRateTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalResponseRateNonTargetLesion)
class ClinicalResponseRateNonTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalResponseRateNonTargetLesion)
class PathologicalResponseRateNonTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(RadiologicalResponseRateNonTargetLesion)
class RadiologicalResponseRateNonTargetLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalResponseRateNewLesion)
class ClinicalResponseRateNewLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalResponseRateNewLesion)
class PathologicalResponseRateNewLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(RadiologicalResponseRateNewLesion)
class RadiologicalResponseRateNewLesionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalResponseRateResult)
class ClinicalResponseRateResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalResponseRateResult)
class PathologicalResponseRateResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(RadiologicalResponseRateResult)
class RadiologicalResponseRateResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalResponseRateCalculationRecords)
class ClinicalResponseRateCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'target_lesion', 'non_target_lesion', 'new_lesion', 'result', 'created_at', 'updated_at')
    search_fields = ('target_lesion',)
    list_per_page = 50
    list_display_links = ('id', 'target_lesion')

@admin.register(PathologicalResponseRateCalculationRecords)
class PathologicalResponseRateCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'target_lesion', 'non_target_lesion', 'new_lesion', 'result', 'created_at', 'updated_at')
    search_fields = ('target_lesion',)
    list_per_page = 50
    list_display_links = ('id', 'target_lesion')


@admin.register(RadiologicalResponseRateCalculationRecords)
class RadiologicalResponseRateCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'target_lesion', 'non_target_lesion', 'new_lesion', 'result', 'created_at', 'updated_at')
    search_fields = ('target_lesion',)
    list_per_page = 50
    list_display_links = ('id', 'target_lesion')






@admin.register(SurgeryModalityRecords)
class SurgeryModalityRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Surgeries)
class SurgeriesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'modality', 'surgery_date', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'modality')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'modality')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(IHCRecords)
class IHCRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHCResults)
class IHCResultsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(IHC_ER)
class IHC_ERAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_PR)
class IHC_PRAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_HER2)
class IHC_HER2Admin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_FISH)
class IHC_FISHAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_Synaptophysin)
class IHC_SynaptophysinAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')
@admin.register(IHC_Chromogranin)
class IHC_ChromograninAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_GATA)
class IHC_GATAAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC_Others)
class IHC_OthersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(IHC)
class IHCAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'ER', 'PR', 'HER2', 'FISH', 'Synaptophysin', 'Chromogranin', 'GATA', 'others', 'created_at', 'updated_at')
    search_fields = ('patient_observation_id', 'ER', 'PR', 'HER2', 'FISH', 'Synaptophysin', 'Chromogranin', 'GATA', 'others')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'ER', 'PR', 'HER2', 'FISH', 'Synaptophysin', 'Chromogranin', 'GATA', 'others')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(Path_lvsi)
class Path_lvsiAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Path_Pni)
class Path_PniAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Path_Margin)
class Path_MarginAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(Path_Ki67)
class Path_Ki67Admin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(StagingPathologicalsDetails)
class StagingPathologicalsDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'lvsi', 'pni', 'margin', 'ki67', 'created_at', 'updated_at')
    search_fields = ('lvsi', 'pni', 'margin', 'ki67', 'patient_observation_id')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(TumourGrade)
class TumourGradeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(DiseaseProgressionStatus)
class DiseaseProgressionStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(SurvivalStatus)
class SurvivalStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PFSStatus)
class PFSStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'status', 'date', 'created_at', 'updated_at') 
    search_fields = ('status', 'date', 'patient_observation_id')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'status', 'date')
    autocomplete_fields = ('patient_observation_id',)

@admin.register(OSStatus)
class OSStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 'status', 'date', 'created_at', 'updated_at') 
    search_fields = ('status', 'date', 'patient_observation_id')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 'status', 'date')
    autocomplete_fields = ('patient_observation_id',)





#--------------------------------- TNM Staging Starts Here ---------------------------------#


# @admin.register(TNMStagingType)
# class TNMStagingTypeAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name', 'created_at', 'updated_at')
#     search_fields = ('name',)
#     list_per_page = 50
#     list_display_links = ('id', 'name')

@admin.register(ClinicalTNMStagingT)
class ClinicalTNMStagingTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalTNMStagingN)
class ClinicalTNMStagingNAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalTNMStagingM)
class ClinicalTNMStagingMAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalTNMStagingResult)
class ClinicalTNMStagingResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(ClinicalTNMStagingCalculationRecords)
class ClinicalTNMStagingCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 't', 'n', 'm', 'result', 'created_at', 'updated_at')
    search_fields = ('result',)
    list_per_page = 50
    list_display_links = ('id', 'result')
@admin.register(StagingClinicals)
class StagingClinicalsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 't', 'n', 'm', 'result', 'date')
    search_fields = ('patient_observation_id', 't', 'n', 'm', 'result')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 't', 'n', 'm', 'result')
    autocomplete_fields = ('patient_observation_id',)

#----------------------------------- Pathological Staging Starts Here -----------------------------------#
@admin.register(PathologicalTNMStagingT)
class PathologicalTNMStagingTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalTNMStagingN)
class PathologicalTNMStagingNAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalTNMStagingM)
class ClinicalTNMStagingMAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalTNMStagingResult)
class ClinicalTNMStagingResultAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_per_page = 50
    list_display_links = ('id', 'name')

@admin.register(PathologicalTNMStagingCalculationRecords)
class PathologicalTNMStagingCalculationRecordsAdmin(ImportExportModelAdmin):
    list_display = ('id', 't', 'n', 'm', 'result', 'created_at', 'updated_at')
    search_fields = ('result',)
    list_per_page = 50
    list_display_links = ('id','result')

@admin.register(StagingPathologicals)
class StagingPathologicalsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'patient_observation_id', 't', 'n', 'm', 'result', 'date')
    search_fields = ('patient_observation_id', 't', 'n', 'm', 'result')
    list_per_page = 50
    list_display_links = ('id', 'patient_observation_id', 't', 'n', 'm', 'result')
    autocomplete_fields = ('patient_observation_id',)

#----------------------------------- Pathological Staging Ends Here -----------------------------------#

#----------------------------------- Patient Ovservation STARTS Here -----------------------------------#


@admin.register(PatientObservation)
class PatientObservationAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'patient_id', 'doctor_id', 'center_id', 'time', 'registration_number',
        'laterality', 'grade',  'current_chemo_protocol', 'chemo_starting_date',
        'chemo_cycle_no', 'disease_progression_status', 'disease_progression_status_date',
        'pfs', 'survival_status', 'survival_status_date', 'overall_survival',
        'line_of_treatment', 'diagnosis_disease_group', 'diagnosis_subgroup',
        'diagnosis_primary_site', 'diagnosis_laterility', 'clinical_response_rate_result',
        'radiological_response_rate_result', 'pathological_response_rate_result',
        'cancer_type', 'created_at', 'updated_at'
    )    
    search_fields = (
        'patient_id__name', 'doctor_id__name', 'center_id__name', 'id' 
    )
    list_filter = ('created_at', 'updated_at')
    list_per_page = 10
    list_display_links = ('id', 'patient_id', 'doctor_id')
    autocomplete_fields = ('patient_id', 'doctor_id')


#----------------------------------- Patient Ovservation ENDS Here -----------------------------------#

# @admin.register(AllData)
# class AllDataAdmin(ImportExportModelAdmin):
#     list_display = ('patient_observation', 'cancer_marker', 'diagnosis', 'staging_pathologicals', 'os_status')
#     search_fields = ('patient_observation__id',)
#     list_filter = ('diagnosis', 'os_status')
#     list_per_page = 15

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AllData  # Import your AllData model
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from oncoedu.models import PatientObservation, CancerMarker, Diagnosis, StagingPathologicals, OSStatus  # Import the models


class AllDataResource(resources.ModelResource):
    """
    Define the resource for AllData for import/export.  This is crucial
    for controlling how related fields are handled during export.
    """
    patient_observation = fields.Field(
        column_name='Patient Observation ID',
        attribute='patient_observation',
        widget=ForeignKeyWidget(PatientObservation, 'id')  # Export PatientObservation ID
    )
    #  For other foreign keys, specify what data you want to export.  Here's how to
    #  export the name of the related CancerMarker, for example:
    cancer_marker = fields.Field(
        column_name='Cancer Marker Name',
        attribute='cancer_marker',
        widget=ForeignKeyWidget(CancerMarker, 'name')  # Export CancerMarker name
    )
    diagnosis = fields.Field(
        column_name='Diagnosis Name',
        attribute='diagnosis',
        widget=ForeignKeyWidget(Diagnosis, 'name')
    )
    staging_pathologicals = fields.Field(
        column_name='Staging Pathologicals',
        attribute='staging_pathologicals',
        widget=ForeignKeyWidget(StagingPathologicals, 'id') #or any other field
    )
    os_status = fields.Field(
        column_name='OS Status',
        attribute='os_status',
        widget=ForeignKeyWidget(OSStatus, 'status')
    )

    class Meta:
        model = AllData
        fields = ('patient_observation', 'cancer_marker', 'diagnosis', 'staging_pathologicals', 'os_status')
        export_order = ('patient_observation', 'cancer_marker', 'diagnosis', 'staging_pathologicals', 'os_status')

@admin.register(AllData)
class AllDataAdmin(ImportExportModelAdmin):
    """
    Admin interface for AllData model with import/export functionality.
    """
    resource_class = AllDataResource  # Use the defined resource class
    list_display = ('patient_observation', 'cancer_marker', 'diagnosis', 'staging_pathologicals', 'os_status')
    search_fields = ('patient_observation__id',)
    list_filter = ('diagnosis', 'os_status')
    list_per_page = 15

    def export_to_csv(self, request, queryset):
        """
        Custom action to export selected AllData objects to CSV.
        This is now redundant, given the use of ImportExportModelAdmin,
        but is retained as an example of a custom admin action.  It's
        generally better to use the library's built-in export functionality.
        """
        import csv
        from django.http import HttpResponse
        from io import StringIO

        #  Use a StringIO object to write to a string in memory
        output = StringIO()
        writer = csv.writer(output)

        # Define the CSV file name.
        filename = "alldata_export.csv"

        # Add all the fields you want in the CSV.  Include fields from related models.
        headers = [
            'PatientObservation ID', 'Patient Name', 'Observation Time',
            'Cancer Marker Name', 'Cancer Marker Value', 'Cancer Marker Unit', 'Cancer Marker Date',
            'Chemotherapy Modalities',
            'Chemotherapy Protocol Cycle', 'Chemotherapy Protocol Type',
            'Clock Position Name',
            'Comorbidity Name',
            'Diagnosis Name',
            'Diagnosis Group ER', 'Diagnosis Group PR', 'Diagnosis Group HER2', 'Diagnosis Group KI67', 'Diagnosis Group Result',
            'Molecular Pathologies Name',
            'Past Treatment Histories Details',
            'Patient History Details',
            'Radiotherapy Schedules Start Date', 'Radiotherapy Schedules End Date', 'Radiotherapy Schedules Intent',
            'Surgeries Surgery Date', 'Surgeries Modality',
            'IHC ER', 'IHC PR', 'IHC HER2', 'IHC FISH',
            'Staging Pathologicals Details LVSI', 'Staging Pathologicals Details PNI',
            'Staging Pathologicals Details Margin', 'Staging Pathologicals Details KI67',
            'PFS Status', 'PFS Date',
            'OS Status', 'OS Date',
            'Staging Clinicals T', 'Staging Clinicals N', 'Staging Clinicals M', 'Staging Clinicals Result', 'Staging Clinicals Date',
            'Staging Pathologicals T', 'Staging Pathologicals N', 'Staging Pathologicals M', 'Staging Pathologicals Result', 'Staging Pathologicals Date'
        ]
        writer.writerow(headers)

        for obj in queryset:
            row = [
                obj.patient_observation.id,
                obj.patient_observation.patient_id.name if obj.patient_observation.patient_id else '',
                obj.patient_observation.time,

                obj.cancer_marker.name.name if obj.cancer_marker and obj.cancer_marker.name else '',
                obj.cancer_marker.value if obj.cancer_marker else '',
                obj.cancer_marker.unit if obj.cancer_marker else '',
                obj.cancer_marker.date if obj.cancer_marker else '',

                obj.chemotherapy_modalities.detail.name if obj.chemotherapy_modalities and obj.chemotherapy_modalities.detail else '',
                obj.chemotherapy_protocol.cycle_no if obj.chemotherapy_protocol else '',
                obj.chemotherapy_protocol.type if obj.chemotherapy_protocol else '',

                # obj.clock_position.name if obj.clock_position else '',
                obj.comorbidity.name.name if obj.comorbidity and obj.comorbidity.name else '',
                # obj.diagnosis.name if obj.diagnosis else '',
                obj.diagnosis_group.er.er_status if obj.diagnosis_group and obj.diagnosis_group.er else '',
                obj.diagnosis_group.pr.pr_status if obj.diagnosis_group and obj.diagnosis_group.pr else '',
                obj.diagnosis_group.her2.her2_status if obj.diagnosis_group and obj.diagnosis_group.her2 else '',
                obj.diagnosis_group.ki67.ki67_status if obj.diagnosis_group and obj.diagnosis_group.ki67 else '',
                obj.diagnosis_group.result.results if obj.diagnosis_group and obj.diagnosis_group.result else '',
                obj.molecular_pathologies.name if obj.molecular_pathologies else '',
                obj.past_treatment_histories.detail if obj.past_treatment_histories else '',
                # obj.patient_history.detail if obj.patient_history else '',
                obj.radiotherapy_schedules.start_date if obj.radiotherapy_schedules else '',
                obj.radiotherapy_schedules.end_date if obj.radiotherapy_schedules else '',
                obj.radiotherapy_schedules.intent.value if obj.radiotherapy_schedules and obj.radiotherapy_schedules.intent else '',
                obj.surgeries.surgery_date if obj.surgeries else '',
                obj.surgeries.modality.name if obj.surgeries and obj.surgeries.modality else '',
                obj.ihc.ER.name if obj.ihc and obj.ihc.ER else '',
                obj.ihc.PR.name if obj.ihc and obj.ihc.PR else '',
                obj.ihc.HER2.name if obj.ihc and obj.ihc.HER2 else '',
                obj.ihc.FISH.name if obj.ihc and obj.ihc.FISH else '',
                obj.staging_pathologicals_details.lvsi.name if obj.staging_pathologicals_details and obj.staging_pathologicals_details.lvsi else '',
                obj.staging_pathologicals_details.pni.name if obj.staging_pathologicals_details and obj.staging_pathologicals_details.pni else '',
                obj.staging_pathologicals_details.margin.name if obj.staging_pathologicals_details and obj.staging_pathologicals_details.margin else '',
                obj.staging_pathologicals_details.ki67.name if obj.staging_pathologicals_details and obj.staging_pathologicals_details.ki67 else '',
                obj.pfs_status.status.name if obj.pfs_status and obj.pfs_status.status else '',
                obj.pfs_status.date if obj.pfs_status else '',
                obj.os_status.status.name if obj.os_status and obj.os_status.status else '',
                obj.os_status.date if obj.os_status else '',
                obj.staging_clinicals.t.name if obj.staging_clinicals and obj.staging_clinicals.t else '',
                obj.staging_clinicals.n.name if obj.staging_clinicals and obj.staging_clinicals.n else '',
                obj.staging_clinicals.m.name if obj.staging_clinicals and obj.staging_clinicals.m else '',
                obj.staging_clinicals.result.name if obj.staging_clinicals and obj.staging_clinicals.result else '',
                obj.staging_clinicals.date if obj.staging_clinicals else '',
                obj.staging_pathologicals.t.name if obj.staging_pathologicals and obj.staging_pathologicals.t else '',
                obj.staging_pathologicals.n.name if obj.staging_pathologicals and obj.staging_pathologicals.n else '',
                obj.staging_pathologicals.m.name if obj.staging_pathologicals and obj.staging_pathologicals.m else '',
                obj.staging_pathologicals.result.name if obj.staging_pathologicals and obj.staging_pathologicals.result else '',
                obj.staging_pathologicals.date if obj.staging_pathologicals else '',
            ]
            writer.writerow(row)

        # Prepare the response
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

    export_to_csv.short_description = "Export to CSV (with related data)"  # set description
    actions = ['export_to_csv']  # Add the action to the admin
