__author__ = 'uwen'

xml_content_starting = u'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE stax SYSTEM "stax.dtd">
<stax>
	<defaultcall function="func_test"/>
	<function name="func_test">
        <sequence>
            <loop from="0" to="0">
                <testcase name="'first_case'">
                    <sequence>
                        <process>
                            <location>'local'</location>
                            <command>'rm'</command>
                            <parms>'-rf D:/codeWorkSpace/PycharmProjects/bush-master/log'</parms>
                        </process>
                        <stafcmd>
                            <location>'local'</location>
                            <service>'fs'</service>
                            <request>'CREATE DIRECTORY D:/codeWorkSpace/PycharmProjects/bush-master/log FULLPATH'</request>
                        </stafcmd>

                        <tcstatus result="'pass'"/>
                    </sequence>
                </testcase>
            </loop>
'''

xml_content = u'''            <loop from="0" to="0">
                <testcase name="'{case.name}'">
                    <sequence>
                        <stafcmd>
                            <location>'192.168.0.100'</location>
                            <service>'event'</service>
                            <request>'generate type monitor subtype properties property status=running property case_name={case.name} property task_name={task_name}'</request>
                        </stafcmd>
                        <process>
                            <location>'local'</location>
                            <command>'{case.command}'</command>
                            <parms>'{script_path}/{case.script} {case.name} {case.param}'</parms>
                        </process>
                        <if expr="RC == 0">
                            <tcstatus result="'pass'"/>
                            <else>
                                <tcstatus result="'fail'"/>
                            </else>
                        </if>
                        <stafcmd>
                            <location>'192.168.0.100'</location>
                            <service>'event'</service>
                            <request>'generate type monitor subtype properties property status=finish property case_name={case.name} property task_name={task_name}'</request>
                        </stafcmd>
                    </sequence>
                </testcase>
            </loop>
'''

xml_content_ending = u'''        <loop from="0" to="0">
                <testcase name="'last_case'">
                    <sequence>
                        <stafcmd>
                            <location>'192.168.0.100'</location>
                            <service>'event'</service>
                            <request>'generate type monitor subtype endoftest'</request>
                        </stafcmd>
                        <stafcmd>
                            <location>'local'</location>
                            <service>'fs'</service>
                            <request>'COPY DIRECTORY D:/codeWorkSpace/PycharmProjects/bush-master/log/ TODIRECTORY {{STAF/Env/HOME}}/log/{0} TOMACHINE 192.168.0.100 RECURSE KEEPEMPTYDIRECTORIES'</request>
                        </stafcmd>
                        <tcstatus result="'pass'"/>
                    </sequence>
                </testcase>
            </loop>
        </sequence>
    </function>
</stax>
'''

import re
import os
from django.conf import settings

tmp_handle_global = None


def generate_xml(task_name, cases, folder_name):
    proj_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # script_path = os.path.join(proj_name, 'media/script')
    script_path = 'D:/codeWorkSpace/PycharmProjects/bush-master/media/script'
    xml_path = settings.MEDIA_ROOT + settings.CASE_DIR
    xml_name = '.'.join([task_name, 'xml'])
    # cases = Suite.objects.get(id=p_suite).case_set.all()
    xml_location = os.path.join(xml_path, xml_name)
    print xml_location

    if os.path.exists(xml_location):
        os.remove(xml_location)
    with open(xml_location, 'a+') as xml_handle:
        xml_handle.write(xml_content_starting)
        for case in cases:
            xml_content_towrite = xml_content.format(case=case, script_path=script_path, task_name=task_name)
            xml_content_towrite = xml_content_towrite.encode('utf')
            xml_handle.write(xml_content_towrite)
        xml_handle.write(xml_content_ending.format(folder_name))