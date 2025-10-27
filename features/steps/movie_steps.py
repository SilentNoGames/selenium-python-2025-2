from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import IMDbHomePage
from pages.imdb_results_page import IMDBResultsPage
from pages.imdb_movie_page import IMDbMoviePage
import time

@given("el usuario esta en el homepage de imdb.com")
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.imdb.com")
    context.imdb_home_page = IMDbHomePage(context.driver)

@when('el usuario busca la pelicula "{movie_name}"')
def step_impl(context, movie_name):
    context.imdb_home_page.search_movie(movie_name)
    context.imdb_results_page = IMDBResultsPage(context.driver)

@when("presiona el link del primer resultado de pelicula")
def step_impl(context):
    context.imdb_results_page.click_first_result()
    context.imdb_movie_page = IMDbMoviePage(context.driver)

@then('su calificacion es "{expected_calification}"')
def step_impl(context, expected_calification):
    actual_calification = context.imdb_movie_page.get_calification()
    assert actual_calification == expected_calification, f"Expected calification {expected_calification}, but got {actual_calification}"

@then('el nombre de la pelicula es "{expected_name}"')
def step_impl(context, expected_name):
    actual_name = context.imdb_movie_page.get_name()
    assert actual_name == expected_name, f"Expected name {expected_name}, but got {actual_name}"


    
