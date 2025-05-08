from django.core.management.base import BaseCommand
from django.apps import apps
from django.utils import timezone
from oncoedu.models import PatientObservation, AllData  # Import your models


class Command(BaseCommand):
    help = "Populates the AllData model with data from existing PatientObservation and related records."

    def handle(self, *args, **options):
        """
        The main logic of the command.  It iterates through all PatientObservation
        instances and creates or updates the corresponding AllData instance
        with data from related models.
        """
        self.stdout.write(self.style.SUCCESS("Starting population of AllData..."))

        # Get all PatientObservation instances.  We'll use prefetch_related
        # to optimize database queries and reduce the number of queries.
        patient_observations = PatientObservation.objects.all().prefetch_related(
            'cancermarker_set',
            'chemotherapymodalities_set',
            'chemotherapyprotocol_set',
            'clockposition_set',
            'comorbidity_set',
            'diagnosis_set',
            'diagnosisgroup_set',
            'molecularpathologies_set',
            'pasttreatmenthistories_set',
            'patienthistory_set',
            'radiotherapyschedules_set',
            'surgeries_set',
            'ihc_set',
            'stagingpathologicalsdetails_set',
            'pfsstatus_set',
            'osstatus_set',
            'stagingclinicals_set',
            'stagingpathologicals_set',
        )

        total_observations = patient_observations.count()
        processed_count = 0

        for po in patient_observations:
            alldata, created = AllData.objects.get_or_create(
                patient_observation_id=po.id)  # changed po to po.id
            # print(f"Processing PatientObservation ID: {po.id}, Created: {created}") #For Debug

            # Use .first() because the foreign keys in AllData are to individual instances, not sets.
            # Get data from the related models, not the model instances themselves.
            alldata.cancer_marker = po.cancermarker_set.first()
            alldata.chemotherapy_modalities = po.chemotherapymodalities_set.first()
            alldata.chemotherapy_protocol = po.chemotherapyprotocol_set.first()
            alldata.clock_position = po.clockposition_set.first()
            alldata.comorbidity = po.comorbidity_set.first()
            alldata.diagnosis = po.diagnosis_set.first()
            alldata.diagnosis_group = po.diagnosisgroup_set.first()
            alldata.molecular_pathologies = po.molecularpathologies_set.first()
            alldata.past_treatment_histories = po.pasttreatmenthistories_set.first()
            alldata.patient_history = po.patienthistory_set.first()
            alldata.radiotherapy_schedules = po.radiotherapyschedules_set.first()
            alldata.surgeries = po.surgeries_set.first()
            alldata.ihc = po.ihc_set.first()
            alldata.staging_pathologicals_details = po.stagingpathologicalsdetails_set.first()
            alldata.pfs_status = po.pfsstatus_set.first()
            alldata.os_status = po.osstatus_set.first()
            alldata.staging_clinicals = po.stagingclinicals_set.first()
            alldata.staging_pathologicals = po.stagingpathologicals_set.first()
            alldata.updated_at = timezone.now()
            alldata.save()

            processed_count += 1
            if processed_count % 100 == 0:  # Print progress every 100 processed records
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Processed {processed_count}/{total_observations} PatientObservations")
                )

        self.stdout.write(self.style.SUCCESS("AllData population complete."))