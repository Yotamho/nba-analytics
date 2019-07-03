from basketball_reference_web_scraper.client import season_schedule

def pbp_for_range(teams, start_year, end_year):
    schedules = map(season_schedule, range(start_year, end_year))
    print("FFF")
    return 5