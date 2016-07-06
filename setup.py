from setuptools import setup

setup(name='adpassword',
   version='2.0',
   description='Password expiration reminder for Active Directory linked workstations',
   url='http://github.com/alfem/adpassword',
   author='Alfonso E.M.',
   author_email='alfonso@el-magnifico.org',
   license='GPL-V2',
   scripts=['bin/ADpassword'],
   packages=['adpassword_support','adpassword_change','adpassword_change_support'],
   zip_safe=False)
                                                