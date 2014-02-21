"""
Fixture data, uses real model data pulled down via the Django ORM
and uses `wasatch.utils.model_to_json` with expand=True
"""

fake_product = {
    'admin': False,
    'archived': False,
    'created_at': '2011-06-07T21:44:36+00:00',
    'email': {
        'backlog': 'backlog-1@items.sprint.ly',
        'defects': 'defects-1@items.sprint.ly',
        'stories': 'stories-1@items.sprint.ly',
        'tasks': 'tasks-1@items.sprint.ly',
        'tests': 'tests-1@items.sprint.ly'
    },
    'id': 1,
    'name': u'sprint.ly'
}

fake_comment_payload = {
    'model': 'Comment',
    'product': fake_product,
    'attributes': {
        'body': u'Bilbo Baggins is a Short Fat Elf.',
        'created_at': '2011-06-11T00:37:07+00:00',
        'created_by': {
            'created_at': '2011-06-07T21:10:52+00:00',
            'email': u'joe@joestump.net',
            'first_name': u'Joe',
            'id': 1L,
            'last_login': '2014-02-14T19:26:54+00:00',
            'last_name': u'Stump'
        },
        'id': 6L,
        'item': {
            'assigned_to': None,
            'created_at': '2011-06-10T17:03:06+00:00',
            'created_by': {
                'created_at': '2011-06-07T21:10:52+00:00',
                'email': u'joe@joestump.net',
                'first_name': u'Joe',
                'id': 1L,
                'last_login': '2014-02-14T19:26:54+00:00',
                'last_name': u'Stump'
            },
            'description': u"Right now we're linking to the Item.pk in the URL. We should be linking and showing the Item.number though.",
            'email': {
                'discussion': 'discussion-34@items.sprint.ly',
                'files': 'files-34@items.sprint.ly'
            },
            'last_modified': '2012-06-15T19:40:06+00:00',
            'number': 33L,
            'product': {
                'archived': False,
                'id': 1L,
                'name': u'sprint.ly'
            },
            'progress': {
                'accepted_at': '2011-10-25T00:37:27+00:00'
            },
            'score': '~',
            'short_url': u'http://sprint.ly/i/1/33/',
            'status': 'accepted',
            'tags': [],
            'title': u'Link to Item.number instead of Item.pk.',
            'type': 'defect'
        },
        'last_modified': '2011-06-11T00:37:07+00:00',
        'type': 'comment'
    }
}

fake_item_payload = {
    'model': 'Item',
    'product': fake_product,
    'attributes': {
        'assigned_to': None,
        'created_at': '2011-06-08T18:11:27+00:00',
        'created_by': {
            'created_at': '2011-06-07T21:10:52+00:00',
            'email': u'joe@joestump.net',
            'first_name': u'Joe',
            'id': 1L,
            'last_login': '2014-02-14T19:26:54+00:00',
            'last_name': u'Stump'
        },
        'description': u'The filter counts in the Backlog, Current, etc. appear to be including sub-items in their counts.',
        'email': {
            'discussion': 'discussion-10@items.sprint.ly',
            'files': 'files-10@items.sprint.ly'
        },
        'last_modified': '2012-06-15T19:40:04+00:00',
        'number': 10L,
        'product': {
            'archived': False,
            'id': 1L,
            'name': u'sprint.ly'
        },
        'progress': {
            'accepted_at': '2011-10-25T00:29:33+00:00'
        },
        'score': 'M',
        'short_url': u'http://sprint.ly/i/1/10/',
        'status': 'accepted',
        'tags': [],
        'title': u"Don't count sub-items in filter counts.",
        'type': 'defect'
    }
}

fake_block_payload = {
    'model': 'Block',
    'product': fake_product,
    'attributes': {
        'blocked': {
            'assigned_to': {
                'created_at': '2011-06-07T21:10:52+00:00',
                'email': u'joe@joestump.net',
                'first_name': u'Joe',
                'id': 1L,
                'last_login': '2014-02-14T19:26:54+00:00',
                'last_name': u'Stump'
            },
            'created_at': '2013-08-21T16:33:10+00:00',
            'created_by': {
               'created_at': '2012-07-23T17:54:30+00:00',
                'email': u'justin@sage.ly',
                'first_name': u'Justin',
                'id': 5304L,
                'last_login': '2014-01-18T00:24:16+00:00',
                'last_name': u'Abrahms'
            },
           'description': '',
           'email': {
                'discussion': 'discussion-495017@items.sprint.ly',
                'files': 'files-495017@items.sprint.ly'
            },
            'last_modified': '2014-01-18T02:01:27+00:00',
            'number': 5318L,
            'parent': {
                'assigned_to': {
                    'created_at': '2011-06-07T21:10:52+00:00',
                    'email': u'joe@joestump.net',
                    'first_name': u'Joe',
                    'id': 1L,
                    'last_login': '2014-02-14T19:26:54+00:00',
                    'last_name': u'Stump'
                },
                'created_at': '2013-08-21T16:31:31+00:00',
                'created_by': {
                    'created_at': '2011-06-07T21:10:52+00:00',
                    'email': u'joe@joestump.net',
                    'first_name': u'Joe',
                    'id': 1L,
                    'last_login': '2014-02-14T19:26:54+00:00',
                    'last_name': u'Stump'
                },
                'description': u"A tracking ticket for things we'd like fixed in our CI process.",
                'email': {
                    'discussion': 'discussion-495015@items.sprint.ly',
                    'files': 'files-495015@items.sprint.ly'
                },
                'last_modified': '2013-10-18T00:25:10+00:00',
                'number': 5317L,
                'product': {
                    'archived': False,
                    'id': 1L,
                    'name': u'sprint.ly'
                },
                'score': '~',
                'short_url': u'http://sprint.ly/i/1/5317/',
                'status': 'someday',
                'tags': [],
                'title': u'As a sprinter, I want a better build process so that functional/unit tests will run on pull request, etc.',
                'type': 'story',
                'what': u'a better build process',
                'who': u'sprinter',
                'why': u'functional/unit tests will run on pull request, etc'
            },
            'product': {
                'archived': False,
                'id': 1L,
                'name': u'sprint.ly'
            },
            'score': '~',
            'short_url': u'http://sprint.ly/i/1/5318/',
            'status': 'backlog',
            'tags': [],
            'title': u"pull requests are tested before they're merged",
            'type': 'task'
        },
        'created_at': '2014-02-19T20:29:23+00:00',
        'id': 4778L,
        'item': {
            'assigned_to': {
                'created_at': '2011-12-10T19:28:42+00:00',
                'email': u'sam@quickleft.com',
                'first_name': u'Sam',
                'id': 298L,
                'last_login': '2013-12-20T03:06:00+00:00',
                'last_name': u'Breed'
            },
            'created_at': '2013-08-02T18:53:42+00:00',
            'created_by': {
                'created_at': '2011-12-10T19:28:42+00:00',
                'email': u'sam@quickleft.com',
                'first_name': u'Sam',
                'id': 298L,
                'last_login': '2013-12-20T03:06:00+00:00',
                'last_name': u'Breed'
            },
            'description': '',
            'email': {
                'discussion': 'discussion-478306@items.sprint.ly',
                'files': 'files-478306@items.sprint.ly'
            },
            'last_modified': '2014-02-19T20:29:23+00:00',
            'number': 5167L,
            'product': {
                'archived': False,
                'id': 1L,
                'name': u'sprint.ly'
            },
            'progress': {
                'started_at': '2013-08-07T16:06:26+00:00',
                'triaged_at': '2013-08-07T16:06:26+00:00'
            },
            'score': '~',
            'short_url': u'http://sprint.ly/i/1/5167/',
            'status': 'in-progress',
            'tags': [],
            'title': u'Update .jshintrc, make JS pass `grunt  jshint`',
            'type': 'task'
        },
        'unblocked': False,
        'user': {
            'created_at': '2011-06-07T21:10:52+00:00',
            'email': u'joe@joestump.net',
            'first_name': u'Joe',
            'id': 1L,
            'last_login': '2014-02-14T19:26:54+00:00',
            'last_name': u'Stump'
        }
    }
}


fake_favorite_payload = {
    'model': 'Favorite',
    'product': fake_product,
    'attributes': {
        'created_at': '2011-06-11T06:41:21+00:00',
        'id': 2,
        'item': {
            'assigned_to': {
                'created_at': '2011-06-07T21:10:52+00:00',
                'email': u'joe@joestump.net',
                'first_name': u'Joe',
                'id': 1,
                'last_login': '2014-02-14T19:26:54+00:00',
                'last_name': u'Stump'
            },
            'created_at': '2011-06-08T18:02:55+00:00',
            'created_by': {
                'created_at': '2011-06-07T21:10:52+00:00',
                'email': u'joe@joestump.net',
                'first_name': u'Joe',
                'id': 1,
                'last_login': '2014-02-14T19:26:54+00:00',
                'last_name': u'Stump'
            },
            'description': u'',
            'email': {
                'discussion': 'discussion-5@items.sprint.ly',
                'files': 'files-5@items.sprint.ly'
            },
            'last_modified': '2012-06-15T19:40:04+00:00',
            'number': 5,
            'product': {
                'archived': False,
                'id': 1,
                'name': u'sprint.ly'
            },
            'progress': {
                'accepted_at': '2011-10-25T00:28:52+00:00'
            },
            'score': '~',
            'short_url': u'http://sprint.ly/i/1/5/',
            'status': 'accepted',
            'tags': [],
            'title': u'As a user, I want Markdown formatting in my descriptions & comments so that I can use advanced formatting without knowing HTML.',
            'type': 'story',
            'what': u'Markdown formatting in my descriptions & comments',
            'who': u'user',
            'why': u'I can use advanced formatting without knowing HTML'
        },
        'user': {
            'created_at': '2011-06-07T21:10:52+00:00',
            'email': u'joe@joestump.net',
            'first_name': u'Joe',
            'id': 1,
            'last_login': '2014-02-14T19:26:54+00:00',
            'last_name': u'Stump'
        }
    }
}

fake_deploy_payload = {
    'model': 'Deploy',
    'product': fake_product,
    'attributes': {
    'environment': u'staging',
    'items': [   {
    'assigned_to': {
    'created_at': '2012-12-18T08:13:43+00:00',
                                        'email': u'fluffaddon@nevir.net',
                                        'first_name': u'Fluffy',
                                        'id': 9708L,
                                        'last_login': '2012-12-26T06:36:08+00:00',
                                        'last_name': u'McFaddon'},
                     'created_at': '2012-12-24T00:02:47+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u'Baby steps.',
                     'email': {
                     'discussion': 'discussion-247159@items.sprint.ly',
                                  'files': 'files-247159@items.sprint.ly'},
                     'last_modified': '2014-01-11T04:44:40+00:00',
                     'number': 1L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'score': 'XL',
                     'short_url': u'http://sprint.ly/i/8094/1/',
                     'status': 'backlog',
                     'tags': [   u'getting started',
                                 u'recruiting',
                                 u'delegation'],
                     'title': u'As an evil genius, I want to recruit a multitude of henchmen so that I am one step closer to taking over the world.',
                     'type': 'story',
                     'what': u'to recruit a multitude of henchmen',
                     'who': u'evil genius',
                     'why': u'I am one step closer to taking over the world'},
                 {
                 'assigned_to': {
                 'created_at': '2012-12-18T08:13:43+00:00',
                                        'email': u'fluffaddon@nevir.net',
                                        'first_name': u'Fluffy',
                                        'id': 9708L,
                                        'last_login': '2012-12-26T06:36:08+00:00',
                                        'last_name': u'McFaddon'},
                     'close_reason': 'fixed',
                     'created_at': '2012-12-24T00:04:00+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u'Be careful not to recruit any trolls; we walk a thin line.',
                     'email': {
                     'discussion': 'discussion-247161@items.sprint.ly',
                                  'files': 'files-247161@items.sprint.ly'},
                     'last_modified': '2012-12-25T19:55:56+00:00',
                     'number': 3L,
                     'parent': 1L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'progress': {
                     'closed_at': '2012-12-25T19:55:56+00:00',
                                     'started_at': '2012-12-25T19:55:46+00:00'},
                     'score': 'XL',
                     'short_url': u'http://sprint.ly/i/8094/3/',
                     'status': 'completed',
                     'tags': [],
                     'title': u'Check 4chan for remote henchmen',
                     'type': 'task'},
                 {
                 'assigned_to': {
                 'created_at': '2012-12-18T08:13:43+00:00',
                                        'email': u'fluffaddon@nevir.net',
                                        'first_name': u'Fluffy',
                                        'id': 9708L,
                                        'last_login': '2012-12-26T06:36:08+00:00',
                                        'last_name': u'McFaddon'},
                     'created_at': '2012-12-24T00:05:30+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u"We've got a few resumes still on file",
                     'email': {
                     'discussion': 'discussion-247162@items.sprint.ly',
                                  'files': 'files-247162@items.sprint.ly'},
                     'last_modified': '2014-01-11T04:44:39+00:00',
                     'number': 4L,
                     'parent': 1L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'score': 'S',
                     'short_url': u'http://sprint.ly/i/8094/4/',
                     'status': 'backlog',
                     'tags': [],
                     'title': u'Reach out to past henchmen',
                     'type': 'task'},
                 {
                 'accepted_by': {
                 'created_at': '2012-12-18T08:19:59+00:00',
                                        'email': u'drbiggles@nevir.net',
                                        'first_name': u'Professor',
                                        'id': 9709L,
                                        'last_login': '2012-12-25T19:56:36+00:00',
                                        'last_name': u'Bigglesworth'},
                     'assigned_to': {
                     'created_at': '2012-12-18T08:19:59+00:00',
                                        'email': u'drbiggles@nevir.net',
                                        'first_name': u'Professor',
                                        'id': 9709L,
                                        'last_login': '2012-12-25T19:56:36+00:00',
                                        'last_name': u'Bigglesworth'},
                     'created_at': '2012-12-24T00:11:57+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u'',
                     'email': {
                     'discussion': 'discussion-247166@items.sprint.ly',
                                  'files': 'files-247166@items.sprint.ly'},
                     'last_modified': '2012-12-25T19:56:57+00:00',
                     'number': 6L,
                     'parent': 1L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'progress': {
                     'accepted_at': '2012-12-25T19:56:56+00:00',
                                     'closed_at': '2012-12-25T19:56:56+00:00',
                                     'started_at': '2012-12-25T19:56:52+00:00'},
                     'score': 'L',
                     'short_url': u'http://sprint.ly/i/8094/6/',
                     'status': 'accepted',
                     'tags': [],
                     'title': u'Set up henching contract w/ Wolfram & Hart',
                     'type': 'task'},
                 {
                 'assigned_to': {
                 'created_at': '2012-12-18T08:13:43+00:00',
                                        'email': u'fluffaddon@nevir.net',
                                        'first_name': u'Fluffy',
                                        'id': 9708L,
                                        'last_login': '2012-12-26T06:36:08+00:00',
                                        'last_name': u'McFaddon'},
                     'created_at': '2012-12-25T20:24:52+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u'',
                     'email': {
                     'discussion': 'discussion-247579@items.sprint.ly',
                                  'files': 'files-247579@items.sprint.ly'},
                     'last_modified': '2014-01-11T04:44:40+00:00',
                     'number': 10L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'score': '~',
                     'short_url': u'http://sprint.ly/i/8094/10/',
                     'status': 'backlog',
                     'tags': [],
                     'title': u'As an evil genius, I want to rob the treasury so that I can fund my evil plots.',
                     'type': 'story',
                     'what': u'to rob the treasury',
                     'who': u'evil genius',
                     'why': u'I can fund my evil plots'},
                 {
                 'assigned_to': {
                 'created_at': '2012-12-18T08:13:43+00:00',
                                        'email': u'fluffaddon@nevir.net',
                                        'first_name': u'Fluffy',
                                        'id': 9708L,
                                        'last_login': '2012-12-26T06:36:08+00:00',
                                        'last_name': u'McFaddon'},
                     'created_at': '2012-12-25T20:30:48+00:00',
                     'created_by': {
                     'created_at': '2012-12-18T08:13:43+00:00',
                                       'email': u'fluffaddon@nevir.net',
                                       'first_name': u'Fluffy',
                                       'id': 9708L,
                                       'last_login': '2012-12-26T06:36:08+00:00',
                                       'last_name': u'McFaddon'},
                     'description': u'',
                     'email': {
                     'discussion': 'discussion-247586@items.sprint.ly',
                                  'files': 'files-247586@items.sprint.ly'},
                     'last_modified': '2014-01-11T04:44:42+00:00',
                     'number': 15L,
                     'parent': 10L,
                     'product': {
                     'archived': False,
                                    'id': 8094L,
                                    'name': u'World Domination'},
                     'score': '~',
                     'short_url': u'http://sprint.ly/i/8094/15/',
                     'status': 'backlog',
                     'tags': [],
                     'title': u'Rally henchmen with moving speech',
                     'type': 'task'}],
    'notes': u'A most EVIL deployment!',
    'user': {
    'created_at': '2012-12-18T08:13:43+00:00',
                'email': u'fluffaddon@nevir.net',
                'first_name': u'Fluffy',
                'id': 9708L,
                'last_login': '2012-12-26T06:36:08+00:00',
                'last_name': u'McFaddon'},
    'version': u'0.27.93'
    }
}


all_payloads = [
    fake_comment_payload,
    fake_item_payload,
    fake_block_payload,
    fake_favorite_payload,
    fake_deploy_payload
]
