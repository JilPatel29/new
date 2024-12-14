from django.core.management.base import BaseCommand
from django.utils.text import slugify
from home.models import BlogPost, CustomUser
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates sample blog posts'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Create a superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        else:
            admin = User.objects.get(username='admin')

        # Sample blog posts
        posts = [
            {
                'title': 'The Art of Wedding Photography',
                'content': """
                Wedding photography is more than just taking pictures – it's about capturing moments that will be cherished for a lifetime. As a wedding photographer, I've learned that every wedding tells a unique story.

                Here are some key aspects of wedding photography:

                1. Preparation Shots
                - Capturing the bride getting ready
                - Detail shots of dress, rings, and accessories
                - Emotional moments with family

                2. Ceremony Coverage
                - The walk down the aisle
                - Exchange of vows
                - First kiss as newlyweds

                3. Reception Highlights
                - First dance
                - Cake cutting
                - Family celebrations

                Remember, the best wedding photos are often the candid ones that capture genuine emotions and unscripted moments.
                """,
                'excerpt': 'Discover the secrets behind capturing perfect wedding moments and creating timeless memories.',
            },
            {
                'title': 'Essential Tips for Pre-Wedding Photoshoots',
                'content': """
                Pre-wedding photoshoots have become an integral part of the wedding journey. They provide couples with beautiful memories and photos they can use for their wedding invitations or display at their reception.

                Key Tips for a Successful Pre-Wedding Shoot:

                1. Location Selection
                - Choose places that are meaningful to you as a couple
                - Consider lighting conditions
                - Mix indoor and outdoor locations

                2. Outfit Planning
                - Coordinate your outfits without matching exactly
                - Bring multiple outfit changes
                - Choose clothes that make you comfortable

                3. Timing is Everything
                - Golden hour (just before sunset) is ideal
                - Schedule enough time between locations
                - Consider weekday shoots for fewer crowds

                4. Be Natural
                - Don't force poses
                - Let your personality shine
                - Trust your photographer's guidance
                """,
                'excerpt': 'Learn how to prepare for and make the most of your pre-wedding photoshoot session.',
            },
            {
                'title': 'Mastering Maternity Photography',
                'content': """
                Maternity photography is about celebrating the beauty of motherhood and capturing this special time in a woman's life. These sessions require a unique approach and understanding.

                Essential Elements of Maternity Photography:

                1. Timing
                - Schedule between 28-34 weeks
                - Morning light for outdoor shoots
                - Multiple short sessions for comfort

                2. Posing Guidelines
                - Flattering angles
                - Natural poses
                - Incorporating family members

                3. Lighting Techniques
                - Soft, diffused light
                - Backlighting for silhouettes
                - Window light for indoor shoots

                4. Props and Accessories
                - Simple props that don't overwhelm
                - Flowing fabrics
                - Personal items with meaning

                The key is to make the mother-to-be feel comfortable and beautiful throughout the session.
                """,
                'excerpt': 'Explore the techniques and considerations for creating beautiful maternity portraits.',
            }
        ]

        for post in posts:
            BlogPost.objects.get_or_create(
                title=post['title'],
                defaults={
                    'slug': slugify(post['title']),
                    'content': post['content'],
                    'excerpt': post['excerpt'],
                    'author': admin,
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully created sample blog posts'))