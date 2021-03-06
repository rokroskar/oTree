# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>

from django_countries.fields import CountryField


class Constants:
    name_in_url = 'survey'
    players_per_group = 1
    number_of_rounds = 1


class Subsession(otree.models.BaseSubsession):

    pass



class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    def q_gender_choices(self):
        return ['Male', 'Female']

    def q_age_choices(self):
        return range(13, 125)

    q_country = CountryField(verbose_name='What is your country of citizenship?')
    q_age = models.PositiveIntegerField(verbose_name='What is your age?', initial=None)
    q_gender = models.CharField(initial=None, verbose_name='What is your gender?', widget=widgets.RadioSelect())

    crt_bat_float = models.DecimalField(max_digits=6, decimal_places=2)
    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()


