from behave import given, when, then
from selenium import webdriver
from pages.lastfm_artist_page import LastFmArtistPage
from pages.lastfm_home_page import LastFmHomePage
from pages.lastfm_results_page import LastFmResultsPage
import time

@given("el usuario está en el home page de last.fm")
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home_page = LastFmHomePage(context.driver)

@when('el usuario busca el artista "{artist_name}"')
def step_impl(context, artist_name):
    context.lastfm_home_page.search_artist(artist_name)
    context.lastfm_results_page = LastFmResultsPage(context.driver)

@when("presiona el link del primer resultado")
def step_impl(context):
    context.lastfm_results_page.press_link()
    context.lastfm_artist_page = LastFmArtistPage(context.driver)

@then('la fecha del ultimo release debe ser "{expected_date}"')
def step_impl(context, expected_date):
    actual_date = context.lastfm_artist_page.get_latest_release()
    assert actual_date == expected_date, f"Expected date {expected_date}, but got {actual_date}"

def after_scenario(context, scenario):
    context.driver.quit()
