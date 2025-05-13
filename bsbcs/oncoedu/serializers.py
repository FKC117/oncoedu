from rest_framework import serializers
from .models import *

from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('created_at', None)
        rep.pop('updated_at', None)
        return rep

class CancerMarkerSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = CancerMarker
        exclude = ['id','created_at', 'updated_at']
class ScocioEconomicStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScocioEconomicStatus
        exclude = ['id','created_at', 'updated_at']
class PatientSerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField()
    socio_economic_status = ScocioEconomicStatusSerializer()
    class Meta:
        model = Patient
        exclude = ['created_at', 'updated_at', 'email', 'nid', 'photo', 'passport']


class BreastExaminationValueRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreastExaminationValueRecord
        exclude = ['id','created_at', 'updated_at']

class CancerMarkerRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancerMarkerRecords
        exclude = ['id','created_at', 'updated_at']


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        exclude = ['id','created_at', 'updated_at']
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        exclude = ['id','created_at', 'updated_at']

class PoliceStationsSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = PoliceStations
        exclude = ['id','created_at', 'updated_at']

class ChemotherapyModalityRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemotherapyModalityRecords
        exclude = ['id','created_at', 'updated_at']

class ChemotherapyProtocolRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemotherapyProtocolRecords
        exclude = ['id','created_at', 'updated_at']

class DiagnosisLateralitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisLaterality
        exclude = ['id','created_at', 'updated_at']

class DiagnosisDiseaseGroupRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisDiseaseGroupRecords
        exclude = ['id','created_at', 'updated_at']

class DiagnosisDiseaseSubGroupRecordsSerializer(serializers.ModelSerializer):
    diagnosis_disease_group = DiagnosisDiseaseGroupRecordsSerializer() 
    class Meta:
        model = DiagnosisDiseaseSubGroupRecords
        exclude = ['id','created_at', 'updated_at']



class ErStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErStatus
        fields = ['id', 'er_status']

class PrStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrStatus
        fields = ['id', 'pr_status']

class Her2StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Her2Status
        fields = ['id', 'her2_status']

class Ki67StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ki67Status
        fields = ['id', 'ki67_status']

class LuminalCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminalCriteria
        exclude = ['id','created_at', 'updated_at']
class DiagnosisGroupRecordsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = DiagnosisGroupRecords
        exclude = ['id','created_at', 'updated_at']
class DiagnosisGroupSerializer(serializers.ModelSerializer):
    er = ErStatusSerializer()
    pr = PrStatusSerializer()
    her2 = Her2StatusSerializer()
    ki67 = Ki67StatusSerializer()
    result = LuminalCriteriaSerializer()
    class Meta:
        model = DiagnosisGroup
        exclude = ['id','created_at', 'updated_at']


class DiagnosisPrimarySiteRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisPrimarySiteRecords
        exclude = ['id','created_at', 'updated_at']

class DiagnosisMetastaticSiteRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisMetastaticSiteRecords
        exclude = ['id','created_at', 'updated_at']

class HistopathologiesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistopathologiesType
        exclude = ['id','created_at', 'updated_at']

class HistopathologyRecordsSerializer(serializers.ModelSerializer):
    type = HistopathologiesTypeSerializer()
    class Meta:
        model = HistopathologyRecords
        exclude = ['id','created_at', 'updated_at']

class LineOfTreatmentRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineOfTreatmentRecords
        exclude = ['id','created_at', 'updated_at']

class MaritalStatusRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatusRecords
        exclude = ['id','created_at', 'updated_at']

class MenstrualCycleRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenstrualCycleRecords
        exclude = ['id','created_at', 'updated_at']

class RadiotherapyScheduleIntentRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiotherapyScheduleIntentRecords
        exclude = ['id','created_at', 'updated_at']

class RadiotherapyScheduleRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiotherapyScheduleRecords
        exclude = ['id','created_at', 'updated_at']

class SurgeryModalityRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryModalityRecords
        exclude = ['id','created_at', 'updated_at']

class IHCRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHCRecords
        exclude = ['id','created_at', 'updated_at']

class IHCResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHCResults
        exclude = ['id','created_at', 'updated_at']

class IHC_ERSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_ER
        exclude = ['id','created_at', 'updated_at']

class IHC_PRSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_PR
        exclude = ['id','created_at', 'updated_at']

class IHC_HER2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_HER2
        exclude = ['id','created_at', 'updated_at']

class IHC_FISHSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_FISH
        exclude = ['id','created_at', 'updated_at']

class IHC_SynaptophysinSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_Synaptophysin
        exclude = ['id','created_at', 'updated_at']

class IHC_ChromograninSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_Chromogranin
        exclude = ['id','created_at', 'updated_at']

class IHC_GATASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_GATA
        exclude = ['id','created_at', 'updated_at']

class IHC_OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHC_Others
        exclude = ['id','created_at', 'updated_at']

class Path_lvsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path_lvsi
        exclude = ['id','created_at', 'updated_at']

class Path_PniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path_Pni
        exclude = ['id','created_at', 'updated_at']

class Path_MarginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path_Margin
        exclude = ['id','created_at', 'updated_at']

class Path_Ki67Serializer(serializers.ModelSerializer):
    class Meta:
        model = Path_Ki67
        exclude = ['id','created_at', 'updated_at']

class TumourGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TumourGrade
        fields = ['name']

class DiseaseProgressionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseProgressionStatus
        exclude = ['id','created_at', 'updated_at']
class SurvivalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurvivalStatus
        exclude = ['id','created_at', 'updated_at']

class ResponseRateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseRateType
        exclude = ['id','created_at', 'updated_at']

class ClinicalResponseRateTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalResponseRateTargetLesion
        exclude = ['id','created_at', 'updated_at']

class PathologicalResponseRateTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalResponseRateTargetLesion
        exclude = ['id','created_at', 'updated_at']

class RadiologicalResponseRateTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologicalResponseRateTargetLesion
        exclude = ['id','created_at', 'updated_at']

class ClinicalResponseRateNonTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalResponseRateNonTargetLesion
        exclude = ['id','created_at', 'updated_at']

class PathologicalResponseRateNonTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalResponseRateNonTargetLesion
        exclude = ['id','created_at', 'updated_at']

class RadiologicalResponseRateNonTargetLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologicalResponseRateNonTargetLesion
        exclude = ['id','created_at', 'updated_at']

class ClinicalResponseRateNewLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalResponseRateNewLesion
        exclude = ['id','created_at', 'updated_at']

class PathologicalResponseRateNewLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalResponseRateNewLesion
        exclude = ['id','created_at', 'updated_at']

class RadiologicalResponseRateNewLesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologicalResponseRateNewLesion
        exclude = ['id','created_at', 'updated_at']

class ClinicalResponseRateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalResponseRateResult
        exclude = ['id','created_at', 'updated_at']

class PathologicalResponseRateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalResponseRateResult
        exclude = ['id','created_at', 'updated_at']

class RadiologicalResponseRateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologicalResponseRateResult
        exclude = ['id','created_at', 'updated_at']

class ClinicalTNMStagingTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalTNMStagingT
        exclude = ['id','created_at', 'updated_at']

class ClinicalTNMStagingNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalTNMStagingN
        exclude = ['id','created_at', 'updated_at']

class ClinicalTNMStagingMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalTNMStagingM
        exclude = ['id','created_at', 'updated_at']

class ClinicalTNMStagingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalTNMStagingResult
        exclude = ['id','created_at', 'updated_at']

class PathologicalTNMStagingTSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalTNMStagingT
        exclude = ['id','created_at', 'updated_at']

class PathologicalTNMStagingNSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalTNMStagingN
        exclude = ['id','created_at', 'updated_at']

class PathologicalTNMStagingMSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalTNMStagingM
        exclude = ['id','created_at', 'updated_at']

class PathologicalTNMStagingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologicalTNMStagingResult
        exclude = ['id','created_at', 'updated_at']



class ChemotherapyModalitiesSerializer(serializers.ModelSerializer):
    detail = ChemotherapyModalityRecordsSerializer()
    class Meta:
        model = ChemotherapyModalities
        exclude = ['id','created_at', 'updated_at']
class ChemotherapyProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemotherapyProtocol
        exclude = ['id','created_at', 'updated_at']
class ClockPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockPosition
        exclude = ['id','created_at', 'updated_at']
class ComorbityRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComorbidityRecords
        exclude = ['id','created_at', 'updated_at']
class ComorbiditySerializer(serializers.ModelSerializer):
    name = ComorbityRecordsSerializer()
    class Meta:
        model = Comorbidity
        exclude = ['id','created_at', 'updated_at']
class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        exclude = ['id','created_at', 'updated_at']

class MolecularPathologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MolecularPathologies
        exclude = ['id','created_at', 'updated_at']

class PastTreatmentHistoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastTreatmentHistories
        exclude = ['id','created_at', 'updated_at']

class RadiotherapySchedulesSerializer(serializers.ModelSerializer):
    intent = RadiotherapyScheduleIntentRecordsSerializer()
    class Meta:
        model = RadiotherapySchedules
        exclude = ['id','created_at', 'updated_at']

class SurgeriesSerializer(serializers.ModelSerializer):
    modality = SurgeryModalityRecordsSerializer()
    class Meta:
        model = Surgeries
        exclude = ['id','created_at', 'updated_at']
class IHCSerializer(serializers.ModelSerializer):
    ER = IHC_ERSerializer()
    PR = IHC_PRSerializer()
    HER2 = IHC_HER2Serializer()
    FISH = IHC_FISHSerializer()
    Synaptophysin = IHC_SynaptophysinSerializer()
    Chromogranin = IHC_ChromograninSerializer()
    GATA = IHC_GATASerializer()
    others = IHC_OthersSerializer()
    class Meta:
        model = IHC
        exclude = ['id','created_at', 'updated_at']

class StagingPathologicalsDetailsSerializer(serializers.ModelSerializer):
    lvsi = Path_lvsiSerializer()
    pni = Path_PniSerializer()
    margin = Path_MarginSerializer()
    ki67 = Path_Ki67Serializer()
    class Meta:
        model = StagingPathologicalsDetails
        exclude = ['id','created_at', 'updated_at']

class PFSStatusSerializer(serializers.ModelSerializer):
    status = DiseaseProgressionStatusSerializer()
    class Meta:
        model = PFSStatus
        exclude = ['id','created_at', 'updated_at']

class OSStatusSerializer(serializers.ModelSerializer):
    status = SurvivalStatusSerializer()
    class Meta:
        model = OSStatus
        exclude = ['id','created_at', 'updated_at']
    
class StagingClinicalsSerializer(serializers.ModelSerializer):
    t = ClinicalTNMStagingTSerializer()
    n = ClinicalTNMStagingNSerializer()
    m = ClinicalTNMStagingMSerializer()
    result = ClinicalTNMStagingResultSerializer()
    class Meta:
        model = StagingClinicals
        exclude = ['id','created_at', 'updated_at']

class StagingPathologicalsSerializer(serializers.ModelSerializer):
    t = PathologicalTNMStagingTSerializer()
    n = PathologicalTNMStagingNSerializer()
    m = PathologicalTNMStagingMSerializer()
    result = PathologicalTNMStagingResultSerializer()
    class Meta:
        model = StagingPathologicals
        exclude = ['id','created_at', 'updated_at']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name',]
# Required Serializers for nested serializers
class ContraceptiveMethodRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContraceptiveMethodRecords
        exclude = ['id','created_at', 'updated_at']
class PatientHistorySerializer(serializers.ModelSerializer):
    marital_status = MaritalStatusRecordsSerializer()
    contraceptive_method = ContraceptiveMethodRecordsSerializer()
    regular_irregular_menstruation = MenstrualCycleRecordsSerializer()
    breast_examination_value = BreastExaminationValueRecordSerializer()

    class Meta:
        model = PatientHistory
        exclude = ['id', 'created_at', 'updated_at']





class PatientObservationSerializer(serializers.ModelSerializer):
    patient_id = PatientSerializer()
    doctor_id = DoctorSerializer()
    center_id = CenterSerializer()
    grade = TumourGradeSerializer()
    disease_progression_status = DiseaseProgressionStatusSerializer()
    survival_status = SurvivalStatusSerializer()
    line_of_treatment = LineOfTreatmentRecordsSerializer()
    diagnosis_disease_group = DiagnosisDiseaseGroupRecordsSerializer()
    diagnosis_subgroup = DiagnosisDiseaseSubGroupRecordsSerializer()
    diagnosis_primary_site = DiagnosisPrimarySiteRecordsSerializer()
    diagnosis_laterility = DiagnosisLateralitySerializer()
    clinical_response_rate_target_lasion = ClinicalResponseRateTargetLesionSerializer()
    clinical_response_rate_non_target_lasion = ClinicalResponseRateNonTargetLesionSerializer()
    clinical_response_rate_new_lasion = ClinicalResponseRateNewLesionSerializer()
    clinical_response_rate_result = ClinicalResponseRateResultSerializer()
    radiological_response_rate_target_lasion = RadiologicalResponseRateTargetLesionSerializer()
    radiological_response_rate_non_target_lasion = RadiologicalResponseRateNonTargetLesionSerializer()
    radiological_response_rate_new_lasion = RadiologicalResponseRateNewLesionSerializer()
    radiological_response_rate_result = RadiologicalResponseRateResultSerializer()
    pathological_response_rate_target_lasion = PathologicalResponseRateTargetLesionSerializer()
    pathological_response_rate_non_target_lasion = PathologicalResponseRateNonTargetLesionSerializer()
    pathological_response_rate_new_lasion = PathologicalResponseRateNewLesionSerializer()
    pathological_response_rate_result = PathologicalResponseRateResultSerializer()
    class Meta:
        model = PatientObservation
        exclude = ['created_at', 'updated_at']

# Nested serializer for AllData
class AllDataSerializer(serializers.ModelSerializer):
    patient_observation = PatientObservationSerializer()
    cancer_marker = CancerMarkerSerializer()
    chemotherapy_modalities = ChemotherapyModalitiesSerializer()
    chemotherapy_protocol = ChemotherapyProtocolSerializer()
    clock_position = ClockPositionSerializer()
    comorbidity = ComorbiditySerializer()
    diagnosis = DiagnosisSerializer()
    diagnosis_group = DiagnosisGroupSerializer()
    molecular_pathologies = MolecularPathologiesSerializer()
    past_treatment_histories = PastTreatmentHistoriesSerializer()
    patient_history = PatientHistorySerializer()
    radiotherapy_schedules = RadiotherapySchedulesSerializer()
    surgeries = SurgeriesSerializer()
    ihc = IHCSerializer()
    staging_pathologicals_details = StagingPathologicalsDetailsSerializer()
    pfs_status = PFSStatusSerializer()
    os_status = OSStatusSerializer()
    staging_clinicals = StagingClinicalsSerializer()
    staging_pathologicals = StagingPathologicalsSerializer()

    class Meta:
        model = AllData
        fields = '__all__'

