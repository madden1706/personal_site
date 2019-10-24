from data_vis.models import DataVis
from django.utils import timezone
import datetime

def create_posts():

    data_vis = DataVis.objects.filter(title_of_post='Title of data_vis 0')    

    if not data_vis:
        print("No posts.")

        for i in range(0,5):
            post = DataVis(
                    title_of_post = f"Title of data_vis {i}",
                    date_of_post = timezone.now() - datetime.timedelta(days=i),
                    seo_description = "SEO",
                    publish = True,
                    intro_text = f'Intro text of data_vis {i}',
                    template_to_use = 'bokeh',
                    homepage_chart_image = '',
                )        
            post.save()
        print("Made test data_vis posts.")

        future_post = DataVis(
                    title_of_post = f"Title of Future Post data_vis",
                    date_of_post = timezone.now() + datetime.timedelta(days=1000),
                    seo_description = "SEO",
                    publish = True,
                    intro_text = f'Intro text of data_vis {i}',
                    template_to_use = 'Bokeh',
                    homepage_chart_image = '',
                )
        
        future_post.save()
        print("Made future test data_vis posts.")

        not_published = DataVis(
            title_of_post = f"Title of Not Published data_vis",
            date_of_post = timezone.now() - datetime.timedelta(days=1),
            seo_description = "SEO",
            publish = False,
            intro_text = f'Intro text of data_vis {i}',
            template_to_use = 'Bokeh',
            homepage_chart_image = '',
        )

        not_published.save()
        print("Made not published test data_vis posts.")        

    else:
        print("Test posts present.")


def remove_all_posts():

    DataVis.objects.all().delete()
    print("Deleted all test data_vis posts.")
