# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


def variables_for_all_templates(self):
    return {
        # example:
        #'my_field': self.player.my_field,
    }


class MyPage(Page):

    form_model = models.Player
    form_fields = ['my_field']

    def participate_condition(self):
        return True

    template_name = 'my_app/MyPage.html'

    def variables_for_template(self):
        return {
            'my_variable_here': 1,
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    template_name = 'my_app/Results.html'


def pages():
    return [
        MyPage,
        ResultsWaitPage,
        Results
    ]
