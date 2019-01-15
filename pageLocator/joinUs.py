
from page_objects import PageObject, PageElement

#需要pip install page-objects 详情见：https://pypi.org/project/page-objects/1.1.0/

class HomePage(PageObject):
    HomePageAssert = u'新潮传媒集团-专注中产家庭消费升级的领先媒体|电梯电视广告投放'
    JOIN_HOME = PageElement(xpath="//a[@data-v-d5d0bb68 and text()='首页']")
    JOIN_HOME_INPUT = PageElement(xpath="//input[@name='k' and @id='k']")
    JOIN_HOME_BUTTON = PageElement(xpath="//a[@class='searchBtn subButton']")
    JOIN_HOME_ASSERT_BUTTON = PageElement(xpath="//span[text()='职位搜索']")


"""
更多页面元素自定义，待补充
"""

