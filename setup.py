from setuptools import setup

setup(name='adpassword',
   version='2.1',
   description='Password expiration reminder for Active Directory linked workstations',
   url='http://github.com/alfem/adpassword',
   author='Alfonso E.M.',
   author_email='alfonso@el-magnifico.org',
   license='GPL-V2',
   scripts=['bin/ADpassword'],
   packages=['adpassword_support','adpassword_change','adpassword_change_support'],
   data_files=[('share/ADpassword/',['ADpassword.png']),('share/applications/',['ADpassword.desktop']),('share/locale/es/LC_MESSAGES/',['mo/es/ADpassword.mo'])],
   zip_safe=False)
                                                
