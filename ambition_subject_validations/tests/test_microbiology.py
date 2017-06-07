from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, POS, NOT_APPLICABLE, OTHER
from edc_base.utils import get_utcnow

from ..validations import Microbiology


class TestMicrobiologyValidations(TestCase):

    def test_urine_culture_performed_require_urine_culture_results(self):
        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_performed': YES,
                        'urine_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'urine_culture_performed': NO,
                        'urine_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'urine_culture_performed': NO,
                        'urine_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

    def test_pos_urine_culture_results_require_urine_culture_organism(self):
        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': POS,
                        'urine_culture_organism': 'klebsiella_sp'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_other_urine_culture_results_require_urine_organism_other(self):
        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'urine_culture_results': OTHER,
                        'urine_culture_organism_other': 'other organism'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_blood_culture_performed_yes_blood_culture_results(self):
        cleaned_data = {'blood_culture_performed': YES,
                        'blood_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_performed': YES,
                        'blood_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'blood_culture_performed': NO,
                        'blood_culture_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'blood_culture_performed': NO,
                        'blood_culture_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

    def test_pos_blood_culture_results_require_date_blood_taken(self):
        cleaned_data = {'blood_culture_results': POS,
                        'date_blood_taken': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'date_blood_taken': get_utcnow()}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_pos_blood_culture_results_require_blood_culture_organism(self):
        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_results': POS,
                        'blood_culture_organism': 'cryptococcus_neoformans'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_other_blood_culture_organism_require_culture_organism_other(self):
        cleaned_data = {'blood_culture_organism': OTHER,
                        'blood_culture_organism_other': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_organism': OTHER,
                        'blood_culture_organism_other': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_organism': OTHER,
                        'blood_culture_organism_other': 'other organism'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_blood_organism_is_bacteria_require_bacteria_identified(self):
        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': 'staphylococus_aureus'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'blood_culture_organism': 'BACTERIA',
                        'bacteria_identified': OTHER}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_other_bacteria_identified_require_bacteria_identified_other(self):
        cleaned_data = {'bacteria_identified': OTHER,
                        'bacteria_identified_other': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'bacteria_identified': OTHER,
                        'bacteria_identified_other': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'bacteria_identified': OTHER,
                        'bacteria_identified_other': 'other_bacteria'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_pos_sputum_results_culture_require_sputum_results_positive(self):
        cleaned_data = {'sputum_results_culture': POS,
                        'sputum_results_positive': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'sputum_results_culture': POS,
                        'sputum_results_positive': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'sputum_results_culture': POS,
                        'sputum_results_positive': 'Value results_positive'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_tissue_biopsy_taken_require_tissue_biopsy_results(self):
        cleaned_data = {'tissue_biopsy_taken': YES,
                        'tissue_biopsy_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_taken': YES,
                        'tissue_biopsy_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'tissue_biopsy_taken': NO,
                        'tissue_biopsy_results': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

        cleaned_data = {'tissue_biopsy_taken': NO,
                        'tissue_biopsy_results': 'no_growth'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

    def test_pos_tissue_biopsy_results_require_date_biopsy_taken(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'date_biopsy_taken': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_results': POS,
                        'date_biopsy_taken': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_results': POS,
                        'date_biopsy_taken': get_utcnow()}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_pos_tissue_biopsy_results_require_tissue_biopsy_organism(self):
        cleaned_data = {'tissue_biopsy_results': POS,
                        'tissue_biopsy_organism': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_results': POS,
                        'tissue_biopsy_organism': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_results': POS,
                        'tissue_biopsy_organism': 'cryptococcus_neoformans'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())

    def test_other_tissue_biopsy_org_require_tissue_biopsy_org_other(self):
        cleaned_data = {'tissue_biopsy_organism': OTHER,
                        'tissue_biopsy_organism_other': None}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_organism': OTHER,
                        'tissue_biopsy_organism_other': NOT_APPLICABLE}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, microbilogy.clean)

        cleaned_data = {'tissue_biopsy_organism': OTHER,
                        'tissue_biopsy_organism_other': 'tissue organism'}
        microbilogy = Microbiology(cleaned_data=cleaned_data)
        self.assertTrue(microbilogy.clean())



