from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, NORMAL, OTHER, NOT_APPLICABLE

from ..form_validators import RadiologyFormValidator


class TestRadiolodyFormValidator(TestCase):

    def test_cxr_type_none(self):
        options = {'cxr_done': YES,
                   'cxr_date': get_utcnow(),
                   'cxr_type': NOT_APPLICABLE}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_type', form_validator._errors)

    def test_cxr_type_normal(self):
        options = {'cxr_done': NO, 'cxr_type': NORMAL}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_type', form_validator._errors)

    def test_cxr_date_none(self):
        options = {'cxr_done': YES,
                   'cxr_type': 'blah',
                   'cxr_date': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_date', form_validator._errors)

    def test_cxr_date_not_none(self):
        options = {'cxr_done': NO, 'cxr_date': get_utcnow().date}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cxr_date', form_validator._errors)

    def test_infiltrate_location_none(self):
        options = {
            'cxr_done': YES,
            'cxr_date': get_utcnow(),
            'cxr_type': 'infiltrates',
            'infiltrate_location': NOT_APPLICABLE}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infiltrate_location', form_validator._errors)

    def test_infiltrate_location_not_none(self):
        options = {
            'cxr_type': NORMAL, 'infiltrate_location': 'lul'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infiltrate_location', form_validator._errors)

    def test_is_scanned_with_contrast_none(self):
        options = {
            'ct_performed': YES,
            'ct_performed_date': get_utcnow(),
            'scanned_with_contrast': NOT_APPLICABLE}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('scanned_with_contrast', form_validator._errors)

    def test_is_scanned_with_contrast_no(self):
        options = {
            'ct_performed': NO, 'scanned_with_contrast': NO}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('scanned_with_contrast', form_validator._errors)

    def test_ct_performed_date_none(self):
        options = {
            'ct_performed': YES,
            'scanned_with_contrast': YES,
            'ct_performed_date': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('ct_performed_date', form_validator._errors)

    def test_ct_performed_date_not_none(self):
        options = {
            'ct_performed': NO, 'ct_performed_date': get_utcnow().date}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('ct_performed_date', form_validator._errors)

    def test_brain_imaging_reason_none(self):
        options = {
            'ct_performed': YES,
            'scanned_with_contrast': YES,
            'ct_performed_date': get_utcnow(),
            'brain_imaging_reason': NOT_APPLICABLE}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason', form_validator._errors)

    def test_brain_imaging_reason_not_none(self):
        options = {
            'ct_performed': NO, 'brain_imaging_reason': 'new_neurology'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason', form_validator._errors)

    def test_brain_imaging_reason_other_none(self):
        options = {
            'brain_imaging_reason': OTHER,
            'brain_imaging_reason_other': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason_other', form_validator._errors)

    def test_brain_imaging_reason_other_not_none(self):
        options = {
            'brain_imaging_reason': 'new_neurology',
            'brain_imaging_reason_other': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('brain_imaging_reason_other', form_validator._errors)

    def test_are_results_abnormal_none(self):
        options = {
            'ct_performed': YES,
            'scanned_with_contrast': YES,
            'ct_performed_date': get_utcnow(),
            'brain_imaging_reason': YES,
            'are_results_abnormal': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_abnormal', form_validator._errors)

    def test_are_results_abnormal_not_none(self):
        options = {
            'ct_performed': NO,
            'are_results_abnormal': NO}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_abnormal', form_validator._errors)

    def test_abnormal_results_reason_none(self):
        options = {
            'are_results_abnormal': YES,
            'abnormal_results_reason': NOT_APPLICABLE}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason', form_validator._errors)

    def test_abnormal_results_reason_not_none(self):
        options = {
            'are_results_abnormal': NO,
            'abnormal_results_reason': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason', form_validator._errors)

    def test_abnormal_results_reason_other_none(self):
        options = {
            'abnormal_results_reason': OTHER,
            'abnormal_results_reason_other': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason_other', form_validator._errors)

    def test_abnormal_results_reason_other_not_none(self):
        options = {
            'abnormal_results_reason': 'cerebral_oedema',
            'abnormal_results_reason_other': 'tumor'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_reason_other', form_validator._errors)

    def test_if_infarcts_location_none(self):
        options = {
            'abnormal_results_reason': 'infarcts',
            'infarcts_location': None}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infarcts_location', form_validator._errors)

    def test_if_infarcts_location_not_none(self):
        options = {
            'abnormal_results_reason': 'cerebral_oedema',
            'infarcts_location': 'chest'}
        form_validator = RadiologyFormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('infarcts_location', form_validator._errors)
