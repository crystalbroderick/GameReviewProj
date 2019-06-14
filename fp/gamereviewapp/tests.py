from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, datetime
from .models import Game, Review
from .views import GameForm, ReviewForm

# not sure how many I need to make..
class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="Awesome Review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')

class GameTest(TestCase):
   def test_string(self):
       vg=Game(gametitle="Some Cool Title")
       self.assertEqual(str(vg), vg.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Game._meta.db_table), 'game')

class GameFormTest(TestCase):
    def test_gameform_is_valid(self):
        form=GameForm(data={'gametitle': "title1", 'summary' : "game summary"})
        self.assertTrue(form.is_valid())

    def test_gameform_nodate(self):
        form=GameForm(data={'releasedate': ""})
        self.assertTrue(form.is_valid())

    def test_gameform_empty(self):
        form=GameForm(data={'gametitle': ""})
        self.assertFalse(form.is_valid())

    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')
    
    def test_gameForm(self):
        data={
            'gametitle' : 'game1',
            'user' : self.user,
            'releasedate' : datetime.date(2019,5,28),
        }
        form = GameForm(data=data)
        self.assertTrue(form.is_valid)

    def test_gameFormInvalid(self):
        data={
            'gametitle' : 'game1',
            'user' : self.user2,
            'releasedate' : datetime.date(2019,5,28),
        }
        form = GameForm(data=data)
        self.assertFalse(form.is_valid())

class ReviewFormTest(TestCase):
    def test_reviewform_is_valid(self):
        form=ReviewForm(data={'reviewtitle': "title1", 'summary' : "game summary"})
        self.assertTrue(form.is_valid())

def test_game_detail_success(self):
        response = self.client.get(reverse('gamedetail', args=(self.vg.id,)))
        self.assertEqual(response.status_code, 200)

class New_Game_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.vg = Game.objects.create(gametitle='somegame1', user=self.test_user, releasedate='2019-05-13', gamerating='T', genre='fantasy', developer= 'someonecool', players="single-player", summary="the most fun game")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newgame'))
        self.assertRedirects(response, '/accounts/login/?next=/gamereviewapp/newGame/')

    def test_Logged_in_uses_correct_template(self):
        self.login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newgame'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamereviewapp/newgame.html')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
 