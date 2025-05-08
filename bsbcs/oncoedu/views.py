from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class CancerMarkerViewSet(ReadOnlyModelViewSet):
    queryset = CancerMarker.objects.all()
    serializer_class = CancerMarkerSerializer

class PatientViewSet(ReadOnlyModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorView(ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientObservationViewSet(ReadOnlyModelViewSet):
    queryset = PatientObservation.objects.all()
    serializer_class = PatientObservationSerializer

class BreastExaminationValueRecordViewSet(ReadOnlyModelViewSet):
    queryset = BreastExaminationValueRecord.objects.all()
    serializer_class = BreastExaminationValueRecordSerializer

class CancerMarkerRecordsViewSet(ReadOnlyModelViewSet):
    queryset = CancerMarkerRecords.objects.all()
    serializer_class = CancerMarkerRecordsSerializer

class ScocioEconomicStatusViewSet(ReadOnlyModelViewSet):
    queryset = ScocioEconomicStatus.objects.all()
    serializer_class = ScocioEconomicStatusSerializer

class CenterViewSet(ReadOnlyModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

class DistrictViewSet(ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
class ComobidityRecordsView(ReadOnlyModelViewSet):
    queryset = ComorbidityRecords.objects.all()
    serializer_class = ComorbityRecordsSerializer

class ComorbidityView(ReadOnlyModelViewSet):
    queryset = Comorbidity.objects.all()
    serializer_class = ComorbiditySerializer
class PoliceStationsViewSet(ReadOnlyModelViewSet):
    queryset = PoliceStations.objects.all()
    serializer_class = PoliceStationsSerializer

class ChemotherapyModalityRecordsViewSet(ReadOnlyModelViewSet):
    queryset = ChemotherapyModalityRecords.objects.all()
    serializer_class = ChemotherapyModalityRecordsSerializer

class ChemotherapyProtocolRecordsViewSet(ReadOnlyModelViewSet):
    queryset = ChemotherapyProtocolRecords.objects.all()
    serializer_class = ChemotherapyProtocolRecordsSerializer

class DiagnosisLateralityViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisLaterality.objects.all()
    serializer_class = DiagnosisLateralitySerializer

class DiagnosisDiseaseGroupRecordsViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisDiseaseGroupRecords.objects.all()
    serializer_class = DiagnosisDiseaseGroupRecordsSerializer

class DiagnosisDiseaseSubGroupRecordsViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisDiseaseSubGroupRecords.objects.all()
    serializer_class = DiagnosisDiseaseSubGroupRecordsSerializer

class DiagnosisGroupRecordsViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisGroupRecords.objects.all()
    serializer_class = DiagnosisGroupRecordsSerializer

class ErStatusViewSet(ReadOnlyModelViewSet):
    queryset = ErStatus.objects.all()
    serializer_class = ErStatusSerializer

class PrStatusViewSet(ReadOnlyModelViewSet):
    queryset = PrStatus.objects.all()
    serializer_class = PrStatusSerializer

class Her2StatusViewSet(ReadOnlyModelViewSet):
    queryset = Her2Status.objects.all()
    serializer_class = Her2StatusSerializer

class Ki67StatusViewSet(ReadOnlyModelViewSet):
    queryset = Ki67Status.objects.all()
    serializer_class = Ki67StatusSerializer

class LuminalCriteriaViewSet(ReadOnlyModelViewSet):
    queryset = LuminalCriteria.objects.all()
    serializer_class = LuminalCriteriaSerializer
class DiagnosisView(ReadOnlyModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
class DiagnosisPrimarySiteRecordsViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisPrimarySiteRecords.objects.all()
    serializer_class = DiagnosisPrimarySiteRecordsSerializer

class DiagnosisMetastaticSiteRecordsViewSet(ReadOnlyModelViewSet):
    queryset = DiagnosisMetastaticSiteRecords.objects.all()
    serializer_class = DiagnosisMetastaticSiteRecordsSerializer

class HistopathologiesTypeViewSet(ReadOnlyModelViewSet):
    queryset = HistopathologiesType.objects.all()
    serializer_class = HistopathologiesTypeSerializer

class HistopathologyRecordsViewSet(ReadOnlyModelViewSet):
    queryset = HistopathologyRecords.objects.all()
    serializer_class = HistopathologyRecordsSerializer

class LineOfTreatmentRecordsViewSet(ReadOnlyModelViewSet):
    queryset = LineOfTreatmentRecords.objects.all()
    serializer_class = LineOfTreatmentRecordsSerializer

class MaritalStatusRecordsViewSet(ReadOnlyModelViewSet):
    queryset = MaritalStatusRecords.objects.all()
    serializer_class = MaritalStatusRecordsSerializer

class MenstrualCycleRecordsViewSet(ReadOnlyModelViewSet):
    queryset = MenstrualCycleRecords.objects.all()
    serializer_class = MenstrualCycleRecordsSerializer

class RadiotherapyScheduleIntentRecordsViewSet(ReadOnlyModelViewSet):
    queryset = RadiotherapyScheduleIntentRecords.objects.all()
    serializer_class = RadiotherapyScheduleIntentRecordsSerializer

class RadiotherapyScheduleRecordsViewSet(ReadOnlyModelViewSet):
    queryset = RadiotherapyScheduleRecords.objects.all()
    serializer_class = RadiotherapyScheduleRecordsSerializer

class SurgeryModalityRecordsViewSet(ReadOnlyModelViewSet):
    queryset = SurgeryModalityRecords.objects.all()
    serializer_class = SurgeryModalityRecordsSerializer

class IHCRecordsViewSet(ReadOnlyModelViewSet):
    queryset = IHCRecords.objects.all()
    serializer_class = IHCRecordsSerializer

class IHCResultsViewSet(ReadOnlyModelViewSet):
    queryset = IHCResults.objects.all()
    serializer_class = IHCResultsSerializer

class IHC_ERViewSet(ReadOnlyModelViewSet):
    queryset = IHC_ER.objects.all()
    serializer_class = IHC_ERSerializer

class IHC_PRViewSet(ReadOnlyModelViewSet):
    queryset = IHC_PR.objects.all()
    serializer_class = IHC_PRSerializer

class IHC_HER2ViewSet(ReadOnlyModelViewSet):
    queryset = IHC_HER2.objects.all()
    serializer_class = IHC_HER2Serializer

class IHC_FISHViewSet(ReadOnlyModelViewSet):
    queryset = IHC_FISH.objects.all()
    serializer_class = IHC_FISHSerializer

class IHC_SynaptophysinViewSet(ReadOnlyModelViewSet):
    queryset = IHC_Synaptophysin.objects.all()
    serializer_class = IHC_SynaptophysinSerializer

class IHC_ChromograninViewSet(ReadOnlyModelViewSet):
    queryset = IHC_Chromogranin.objects.all()
    serializer_class = IHC_ChromograninSerializer

class IHC_GATAViewSet(ReadOnlyModelViewSet):
    queryset = IHC_GATA.objects.all()
    serializer_class = IHC_GATASerializer

class IHC_OthersViewSet(ReadOnlyModelViewSet):
    queryset = IHC_Others.objects.all()
    serializer_class = IHC_OthersSerializer

class Path_lvsiViewSet(ReadOnlyModelViewSet):
    queryset = Path_lvsi.objects.all()
    serializer_class = Path_lvsiSerializer

class Path_PniViewSet(ReadOnlyModelViewSet):
    queryset = Path_Pni.objects.all()
    serializer_class = Path_PniSerializer

class Path_MarginViewSet(ReadOnlyModelViewSet):
    queryset = Path_Margin.objects.all()
    serializer_class = Path_MarginSerializer

class Path_Ki67ViewSet(ReadOnlyModelViewSet):
    queryset = Path_Ki67.objects.all()
    serializer_class = Path_Ki67Serializer

class TumourGradeViewSet(ReadOnlyModelViewSet):
    queryset = TumourGrade.objects.all()
    serializer_class = TumourGradeSerializer

class DiseaseProgressionStatusViewSet(ReadOnlyModelViewSet):
    queryset = DiseaseProgressionStatus.objects.all()
    serializer_class = DiseaseProgressionStatusSerializer

class SurvivalStatusViewSet(ReadOnlyModelViewSet):
    queryset = SurvivalStatus.objects.all()
    serializer_class = SurvivalStatusSerializer

class ResponseRateTypeViewSet(ReadOnlyModelViewSet):
    queryset = ResponseRateType.objects.all()
    serializer_class = ResponseRateTypeSerializer

class ContraceptiveMethodRecordsViewSet(ReadOnlyModelViewSet):
    queryset = ContraceptiveMethodRecords.objects.all()
    serializer_class = ContraceptiveMethodRecordsSerializer

class ClinicalResponseRateTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalResponseRateTargetLesion.objects.all()
    serializer_class = ClinicalResponseRateTargetLesionSerializer

class PathologicalResponseRateTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalResponseRateTargetLesion.objects.all()
    serializer_class = PathologicalResponseRateTargetLesionSerializer

class RadiologicalResponseRateTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = RadiologicalResponseRateTargetLesion.objects.all()
    serializer_class = RadiologicalResponseRateTargetLesionSerializer

class ClinicalResponseRateNonTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalResponseRateNonTargetLesion.objects.all()
    serializer_class = ClinicalResponseRateNonTargetLesionSerializer

class PathologicalResponseRateNonTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalResponseRateNonTargetLesion.objects.all()
    serializer_class = PathologicalResponseRateNonTargetLesionSerializer

class RadiologicalResponseRateNonTargetLesionViewSet(ReadOnlyModelViewSet):
    queryset = RadiologicalResponseRateNonTargetLesion.objects.all()
    serializer_class = RadiologicalResponseRateNonTargetLesionSerializer

class ClinicalResponseRateNewLesionViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalResponseRateNewLesion.objects.all()
    serializer_class = ClinicalResponseRateNewLesionSerializer

class PathologicalResponseRateNewLesionViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalResponseRateNewLesion.objects.all()
    serializer_class = PathologicalResponseRateNewLesionSerializer

class RadiologicalResponseRateNewLesionViewSet(ReadOnlyModelViewSet):
    queryset = RadiologicalResponseRateNewLesion.objects.all()
    serializer_class = RadiologicalResponseRateNewLesionSerializer

class ClinicalResponseRateResultViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalResponseRateResult.objects.all()
    serializer_class = ClinicalResponseRateResultSerializer

class PathologicalResponseRateResultViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalResponseRateResult.objects.all()
    serializer_class = PathologicalResponseRateResultSerializer

class RadiologicalResponseRateResultViewSet(ReadOnlyModelViewSet):
    queryset = RadiologicalResponseRateResult.objects.all()
    serializer_class = RadiologicalResponseRateResultSerializer

class ClinicalTNMStagingTViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalTNMStagingT.objects.all()
    serializer_class = ClinicalTNMStagingTSerializer

class ClinicalTNMStagingNViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalTNMStagingN.objects.all()
    serializer_class = ClinicalTNMStagingNSerializer

class ClinicalTNMStagingMViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalTNMStagingM.objects.all()
    serializer_class = ClinicalTNMStagingMSerializer

class ClinicalTNMStagingResultViewSet(ReadOnlyModelViewSet):
    queryset = ClinicalTNMStagingResult.objects.all()
    serializer_class = ClinicalTNMStagingResultSerializer

class PathologicalTNMStagingTViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalTNMStagingT.objects.all()
    serializer_class = PathologicalTNMStagingTSerializer

class PathologicalTNMStagingNViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalTNMStagingN.objects.all()
    serializer_class = PathologicalTNMStagingNSerializer

class PathologicalTNMStagingMViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalTNMStagingM.objects.all()
    serializer_class = PathologicalTNMStagingMSerializer

class PathologicalTNMStagingResultViewSet(ReadOnlyModelViewSet):
    queryset = PathologicalTNMStagingResult.objects.all()
    serializer_class = PathologicalTNMStagingResultSerializer

class ChemotherapyModalitiesSerializerView(ReadOnlyModelViewSet):
    queryset = ChemotherapyModalities.objects.all()
    serializer_class = ChemotherapyModalitiesSerializer

class ChemotherapyProtocolSerializerView(ReadOnlyModelViewSet):
    queryset = ChemotherapyProtocol.objects.all()
    serializer_class = ChemotherapyProtocolSerializer

class ClockPositionSerializerView(ReadOnlyModelViewSet):
    queryset = ClockPosition.objects.all()
    serializer_class = ClockPositionSerializer

class ComorbiditySerializerView(ReadOnlyModelViewSet):
    queryset = Comorbidity.objects.all()
    serializer_class = ComorbiditySerializer



class MolecularPathologiesSerializerView(ReadOnlyModelViewSet):
    queryset = MolecularPathologies.objects.all()
    serializer_class = MolecularPathologiesSerializer

class PastTreatmentHistoriesSerializerView(ReadOnlyModelViewSet):
    queryset = PastTreatmentHistories.objects.all()
    serializer_class = PastTreatmentHistoriesSerializer

class PatientHistorySerializerView(ReadOnlyModelViewSet):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

class RadiotherapySchedulesSerializerView(ReadOnlyModelViewSet):
    queryset = RadiotherapySchedules.objects.all()
    serializer_class = RadiotherapySchedulesSerializer


class SurgeriesSerializerView(ReadOnlyModelViewSet):
    queryset = Surgeries.objects.all()
    serializer_class = SurgeriesSerializer

class IHCSerializerView(ReadOnlyModelViewSet):
    queryset = IHC.objects.all()
    serializer_class = IHCSerializer

class StagingPathologicalsDetailsSerializerView(ReadOnlyModelViewSet):
    queryset = StagingPathologicalsDetails.objects.all()
    serializer_class = StagingPathologicalsDetailsSerializer

class PFSStatusSerializerView(ReadOnlyModelViewSet):
    queryset = PFSStatus.objects.all()
    serializer_class = PFSStatusSerializer

class OSStatusSerializerView(ReadOnlyModelViewSet):
    queryset = OSStatus.objects.all()
    serializer_class = OSStatusSerializer


class StagingClinicalsSerializerView(ReadOnlyModelViewSet):
    queryset = StagingClinicals.objects.all()
    serializer_class = StagingClinicalsSerializer

class StagingPathologicalsSerializerView(ReadOnlyModelViewSet):
    queryset = StagingPathologicals.objects.all()
    serializer_class = StagingPathologicalsSerializer

class AllDataSerializerView(ReadOnlyModelViewSet):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer







