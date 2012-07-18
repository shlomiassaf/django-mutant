
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from ....models import FieldDefinition, FieldDefinitionManager


DIM_CHOICES = (
    (2, _(u'Two-dimensional')),
    (3, _(u'Three-dimensional')),
)

srid_help_text = _(u'Spatial Reference System Identity')

spatial_index_help_text = _(u'Creates a spatial index for the given '
                            u'geometry field.')

dim_help_text = _(u'Coordinate dimension.')

geography_help_text = _(u'Creates a database column of type geography, '
                        u'rather than geometry.')

class GeometryFieldDefinition(FieldDefinition):

    srid = models.IntegerField(_(u'SRID'), default=4326,
                               help_text=srid_help_text)
    spatial_index = models.BooleanField(_(u'spatial index'), default=True,
                                        help_text=spatial_index_help_text)
    dim = models.PositiveSmallIntegerField(_(u'coordinate dimension'),
                                           choices=DIM_CHOICES, default=2,
                                           help_text=dim_help_text)
    geography = models.BooleanField(_(u'geography'), default=False,
                                    help_text=geography_help_text)

    objects = FieldDefinitionManager()

    class Meta:
        app_label = 'mutant'
        defined_field_options = ('srid', 'spatial_index', 'dim', 'geography')
        defined_field_category = _(u'Geometry')


class PointFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.PointField


class LineStringFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.LineStringField


class PolygonFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.PolygonField


class MultiPointFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.MultiPointField


class MultiLineStringFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.MultiLineStringField


class MultiPolygonFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.MultiPolygonField


class GeometryCollectionFieldDefinition(GeometryFieldDefinition):

    class Meta:
        app_label = 'mutant'
        proxy = True
        defined_field_class = models.GeometryCollectionField
