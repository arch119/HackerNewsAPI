from hn import HN


hn = HN()


def test_stories_dict_structure():
    """
    This test checks if the scraping of the top stories
    worked in general by testing if the stories dict is filled with all
    the values one might expect. It might be better to
    check each value in a separate test but to get
    started this will have to do.
    """
    for story in hn.get_stories():
        # testing for unicode or string
        # because the types are mixed sometimes
        assert type(story['rank']) == int
        assert type(story['story_id']) == int
        assert type(story['title']) in [unicode, str]
        assert type(story['link']) in [unicode, str]
        assert type(story['domain']) in [unicode, str]
        assert type(story['points']) == int
        assert type(story['submitter']) in [unicode, str]
        assert type(story['published_time']) in [unicode, str]
        assert type(story['submitter_profile']) in [unicode, str]
        assert type(story['num_comments']) == int
        assert type(story['comments_link']) in [unicode, str]
        assert type(story['is_self']) == bool


def test_stories_dict_structure_newest():
    """
    This test checks if the scraping of the newest stories
    worked in general by testing if the stories dict is filled with all
    the values one might expect. It might be better to
    check each value in a separate test but to get
    started this will have to do.
    """
    for story in hn.get_stories(story_type='newest'):
        # testing for unicode or string
        # because the types are mixed sometimes
        assert type(story['rank']) == int
        assert type(story['story_id']) == int
        assert type(story['title']) in [unicode, str]
        assert type(story['link']) in [unicode, str]
        assert type(story['domain']) in [unicode, str]
        assert type(story['points']) == int
        assert type(story['submitter']) in [unicode, str]
        assert type(story['published_time']) in [unicode, str]
        assert type(story['submitter_profile']) in [unicode, str]
        assert type(story['num_comments']) == int
        assert type(story['comments_link']) in [unicode, str]
        assert type(story['is_self']) == bool


def test_stories_dict_structure_best():
    """
    This test checks if the scraping of the best stories
    worked in general by testing if the stories dict is filled with all
    the values one might expect. It might be better to
    check each value in a separate test but to get
    started this will have to do.
    """
    for story in hn.get_stories(story_type='best'):
        # testing for unicode or string
        # because the types are mixed sometimes
        assert type(story['rank']) == int
        assert type(story['story_id']) == int
        assert type(story['title']) in [unicode, str]
        assert type(story['link']) in [unicode, str]
        assert type(story['domain']) in [unicode, str]
        assert type(story['points']) == int
        assert type(story['submitter']) in [unicode, str]
        assert type(story['published_time']) in [unicode, str]
        assert type(story['submitter_profile']) in [unicode, str]
        assert type(story['num_comments']) == int
        assert type(story['comments_link']) in [unicode, str]
        assert type(story['is_self']) == bool

def test_stories_dict_length_top():
    """
    This test checks if the dict returned by scraping the front page
    of HN is 30.
    """
    assert len(hn.get_stories()) == 30

def test_stories_dict_length_best():
    """
    This test checks if the dict returned by scraping the best page
    of HN is 30.
    """
    assert len(hn.get_stories(story_type='best')) == 30
    
def test_stories_dict_length_top_newest():
    """
    This test checks if the dict returned by scraping the newest page
    of HN is 30.
    """
    assert len(hn.get_stories(story_type='newest')) == 30