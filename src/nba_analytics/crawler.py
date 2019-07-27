from os.path import join

from basketball_reference_web_scraper.client import season_schedule, play_by_play
from basketball_reference_web_scraper.data import OutputType, OutputWriteOption, TEAM_TO_TEAM_ABBREVIATION


def pbp_for_range(start_year, end_year, path):
    for season in map(season_schedule, range(start_year, end_year + 1)):
        for match in season:
            pbp_for_schedule_record(path)(match)


def format_path(path, match):
    return join(path, TEAM_TO_TEAM_ABBREVIATION[match["away_team"]] + "_" + TEAM_TO_TEAM_ABBREVIATION[
        match["home_team"]]) + "_" + match["start_time"].strftime("%d%m%y") + ".json"


def pbp_for_schedule_record(path):
    return lambda match: play_by_play(
        match["home_team"],
        match["start_time"].day - 1,  # days are zero based
        match["start_time"].month,
        match["start_time"].year,
        OutputType.JSON,
        format_path(path, match),
        OutputWriteOption.WRITE
    )


pbp_for_range(2019, 2019, "/Users/yotamho/data/nba_pbp_2019")
