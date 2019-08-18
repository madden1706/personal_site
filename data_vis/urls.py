from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView 
from .views import DataVisHomepage, data_vis_post
from .models import DataVis as DVModel



app_name = "data_vis"


class CustomArchiveIndexView(ArchiveIndexView):
    """Needed a view to excluded the non-published items."""

    def get_dated_items(self):
        """Return (date_list, items, extra_context) for this request."""
        qs = self.get_dated_queryset()
        qs = qs.filter(publish=True) # Filtering for the the published data.
        date_list = self.get_date_list(qs, ordering='DESC')

        if not date_list:
            qs = qs.none()

        return (date_list, qs, {})



urlpatterns = [
    path('', DataVisHomepage.as_view(), name='data_vis'),
    path('<slug:slug>_<pk>/', data_vis_post, name="data_vis_post"),
    path('archive/',
         CustomArchiveIndexView.as_view(model=DVModel, date_field="date_of_post"),
         name="data_vis_archive"),
   # path('test', test_bokeh,)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# alsa_output.pci-0000_1e_00.3.analog-stereo





