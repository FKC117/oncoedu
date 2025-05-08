from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver

def update_alldata(instance, model_field):
    AllData = apps.get_model('oncoedu', 'AllData')
    po_id = instance.patient_observation_id
    alldata, created = AllData.objects.get_or_create(patient_observation_id=po_id)
    setattr(alldata, model_field, instance)
    alldata.save()

model_map = {
    'CancerMarker': 'cancer_marker',
    'ChemotherapyModalities': 'chemotherapy_modalities',
    'ChemotherapyProtocol': 'chemotherapy_protocol',
    'ClockPosition': 'clock_position',
    'Comorbidity': 'comorbidity',
    'Diagnosis': 'diagnosis',
    'DiagnosisGroup': 'diagnosis_group',
    'MolecularPathologies': 'molecular_pathologies',
    'PastTreatmentHistories': 'past_treatment_histories',
    'PatientHistory': 'patient_history',
    'RadiotherapySchedules': 'radiotherapy_schedules',
    'Surgeries': 'surgeries',
    'IHC': 'ihc',
    'StagingPathologicalsDetails': 'staging_pathologicals_details',
    'PFSStatus': 'pfs_status',
    'OSStatus': 'os_status',
    'StagingClinicals': 'staging_clinicals',
    'StagingPathologicals': 'staging_pathologicals',
}

for model_name, field_name in model_map.items():
    model = apps.get_model('oncoedu', model_name)
    def make_receiver(field):
        @receiver(post_save, sender=model)
        def handler(sender, instance, **kwargs):
            update_alldata(instance, field)
        return handler
    make_receiver(field_name)
