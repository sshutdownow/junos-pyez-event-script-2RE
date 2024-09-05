from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import jcs

data = """
delete policy-options community COMMUNITY_DATAIX_CONTROL members 0:15169
delete policy-options community COMMUNITY_DATAIX_CONTROL members 0:47764
delete policy-options community COMMUNITY_DATAIX_CONTROL members 0:13238
"""

with Device() as dev:
        if("master" in dev.facts["current_re"]):
                with Config(dev) as cu:
                        cu.lock()
                        cu.load(data, format="set")
                        cu.pdiff()
                        if cu.commit_check():
                            cu.commit(comment="Configuration modified through event script bgp_up", timeout=300)
                        else:
                            cu.rollback()
                        cu.unlock()

