from nba_analytics.crawler import pbp_for_range


def test_crawler():
    assert pbp_for_range(3, 2008, 2009) != None
