#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by evo on 10/9/17
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Young]'
    FLASKY_MAIL_SENDER = 'Young Admin<bloodyevo@163.com>'
    FLASKY_ADMIN = os.environ.get('YOUNG_ADMIN')
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 20
    FLASKY_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    )


class ProducingConfig(Config):
    SQLALCHEMY_DATABASE_URL = os.environ.get('Producing_DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'date-pro.sqlite')
    )


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'Producing': ProducingConfig,

    'default': DevelopmentConfig
}
