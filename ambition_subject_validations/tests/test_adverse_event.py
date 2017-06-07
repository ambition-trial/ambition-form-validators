from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import YES, NO, UNKNOWN

from ..form_validators import AdverseEventFormValidator


class TestAdverseEventFormValidatorValidations(TestCase):

    def test_ae_cause_yes(self):
        options = {
            'ae_cause': YES,
            'ae_cause_other': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ae_cause_no(self):
        options = {
            'ae_cause': NO,
            'ae_cause_other': YES}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ae_study_relation_possibility_no(self):
        options = {
            'ae_study_relation_possibility': NO,
            'possiblity_detail': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ae_study_relation_possibility_unknown(self):
        options = {
            'ae_study_relation_possibility': UNKNOWN,
            'possiblity_detail': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ae_study_relation_possibility_yes(self):
        options = {
            'ae_study_relation_possibility': YES,
            'possiblity_detail': NO}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ambisome_relation_none(self):
        options = {
            'ae_study_relation_possibility': YES,
            'ambisome_relation': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_ambisome_relation_yes(self):
        options = {
            'ae_study_relation_possibility': NO,
            'ambisome_relation': YES}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_fluconazole_relation_yes(self):
        options = {
            'ae_study_relation_possibility': YES,
            'fluconazole_relation': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_fluconazole_relation_none(self):
        options = {
            'ae_study_relation_possibility': NO,
            'fluconazole_relation': YES}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_amphotericin_b_relation_none(self):
        options = {
            'ae_study_relation_possibility': YES,
            'amphotericin_b_relation': None}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_amphotericin_b_relation_YES(self):
        options = {
            'ae_study_relation_possibility': NO,
            'amphotericin_b_relation': YES}
        form_validator = AdverseEventFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)
