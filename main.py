import pandas as pd
import json
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts.charts import Radar
from pyecharts.globals import ThemeType
from pyecharts.charts import Page
from pyecharts.charts import TreeMap
from pyecharts.charts import Sunburst
from pyecharts.charts import Funnel
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts
from pyecharts.components import Table


#背景1
image1 = Image()
img_src = (

    "bj2.png"
)
image1.add(
    src=img_src,
    style_opts={"width": "1770px", "height": "1000px"},
)
image1.set_global_opts(
    title_opts=ComponentTitleOpts(title="", subtitle="")
)
image1.render("bj.html")

#背景2
image2 = Image()
img_src = (

    "bj10.png"
)
image2.add(
    src=img_src,
    style_opts={"width": "1450px", "height": "750px"},
)
image2.render("bj2.html")




#散点图
'''data = pd.read_csv(open('sales_month.csv',encoding='gbk'))
month = data['month'].tolist()
sales = data['sales'].tolist()
profit = data['profit'].tolist()

sd = (
    Scatter()
    .add_xaxis(month)
    .add_yaxis("销售额", sales,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("利润", profit,label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        visualmap_opts=opts.VisualMapOpts(type_="color", max_=400000, min_=10000),
    )

)
sd.render("sdt.html")
'''






#地图
data = pd.read_csv(open('sales_province.csv',encoding='gbk'))

provinces = data['province'].tolist()
sales = data['sales'].tolist()
profit = data['profit'].tolist()

a = list(zip(provinces, sales))
b = list(zip(provinces, profit))
map = (
    Map()
    .add("销售额", a, "china")
    .add("利润", b, "china")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),
        title_opts=opts.TitleOpts(title=""),

        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            pieces=[
                {
                    "min": 230001,
                    "label": '>230000',
                    "color": "#516b91"
                },
                {   "max": 230000,
                    "min": 200001,
                    "label": '200000-230000',
                    "color": "#59c4e6"
                },
                {"max": 200000,
                 "min": 180001,
                 "label": '180001-200000',
                 "color": "#edafda"
                 },
                {
                    "max": 180000,
                    "min": 150001,
                    "label": '150001-180000',
                    "color": "#93b7e3"
                },
                {
                    "max": 150000,
                    "min": 100001,
                    "label": '100001-150000',
                    "color": "#a5e7f0"
                },
                {
                    "max": 100000,
                    "min": 60001,
                    "label": '60001-100000',
                    "color": "#cbb0e3"
                },
                {
                    "max": 60000,
                    "min": 30001,
                    "label": '30001-60000',
                    "color": "#e5cf0d"
                },
                {
                    "max": 30000,
                    "min": 9999,
                    "label": '9999-30000',
                    "color": "#97b552"
                },
                {
                    "max": 10000,
                    "min": -35000,
                    "label": '0-10000',
                    "color": "#95706d"
                }
            ]
        )
    )
)

map.render("2.html")







#玫瑰图
data = pd.read_csv("sales_region.csv", encoding="gbk")
region = data["region"].tolist()
sales = data["sales"].tolist()
profit = data["profit"].tolist()

a = list(zip(region, sales))
b = list(zip(region, profit))
pie = (
    Pie({"theme": ThemeType.INFOGRAPHIC})
        .add("销售额",a,
        radius=["50%", "80%"],rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True, position="outside", formatter="{b}: {d}%"),
    )
        .add("利润",b,
        radius=["20%", "30%"],rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False, position="outside", formatter="{b}: {d}%"),
    )
        .set_global_opts(title_opts=opts.TitleOpts(""),legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),)
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ))
)
pie.render("4.1.html")



#雷达图
'''v1 = [[502667.277,558296.522,761143.054,179421.48,222300.092,691845.854]]
v2 = [[553000.637,539760.162,561800.574,117250,199190.872,726870.014]]
radar1 = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="东北", max_=600000),
            opts.RadarIndicatorItem(name="华北", max_=600000),
            opts.RadarIndicatorItem(name="华东", max_=800000),
            opts.RadarIndicatorItem(name="西北", max_=200000),
            opts.RadarIndicatorItem(name="西南", max_=300000),
            opts.RadarIndicatorItem(name="中南", max_=800000),
        ]
    )
    .add("销售额", v1,
        linestyle_opts=opts.LineStyleOpts(width=3),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#f47920"),
         )
    .add("利润", v2,
        linestyle_opts=opts.LineStyleOpts(width=3),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="#905a3d"),
         )
    #.set_colors(["#f47920", "#905a3d"])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(selected_mode="single",textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),
        title_opts=opts.TitleOpts(title=""),


    )

    )

radar1.render("4.html")
'''




#折线图
data = pd.read_csv("sales_month.csv",encoding='gbk')
month = data["month"]
sales= data["sales"]
profit = data["profit"]

line = (
    Line({"theme": ThemeType.INFOGRAPHIC})
    .add_xaxis(month.tolist())
    .add_yaxis("销售额", sales.tolist(),is_smooth=True,symbol="circle",label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),areastyle_opts=opts.AreaStyleOpts(opacity=0.7)
               )
    .add_yaxis("利润", profit.tolist(),is_smooth=True,symbol="circle",label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),areastyle_opts=opts.AreaStyleOpts(opacity=0.7)
               )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
)

line.render("3.html")




#柱状图

data = pd.read_csv("sales_manager.csv",encoding="gbk")
x_data = data["sales_manager"].tolist()
y_sales = data["sales"].tolist()
y_profit = data["profit"].tolist()

bar = (
    Bar({"theme": ThemeType.INFOGRAPHIC})
    .add_xaxis(x_data)
    .add_yaxis("销售额",y_sales,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("利润", y_profit,label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),
        title_opts={"text": ""}

    )
)

bar.render("1.html")




#柱状图2
data = pd.read_csv("sales_province.csv",encoding='gbk')
x_data = data["province"].tolist()
y_sales = data["sales"].tolist()
y_profit = data["profit"].tolist()
bar1 = (
    Bar({"theme": ThemeType.INFOGRAPHIC})
    .add_xaxis(x_data)
    .add_yaxis("销售额", y_sales,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("利润",y_profit,label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),
        datazoom_opts=opts.DataZoomOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    #.set_colors('#426ab3')
)
bar1.render("2.1.html")



#树图
'''with open('sales_product.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
treemap = (
    TreeMap({"theme": ThemeType.INFOGRAPHIC})
    .add(
        "",
        data,
        levels=[
            {"itemStyle": {"borderColor": "#777", "borderWidth": 0, "gapWidth": 1}, "upperLabel": {"show": False}},
            {"itemStyle": {"borderColor": "#555", "borderWidth": 5, "gapWidth": 1}, "upperLabel": {"show": False}},
            {"itemStyle": {"borderColor": "#333", "borderWidth": 5, "gapWidth": 1}, "upperLabel": {"show": True}}
        ],
        roam=False,
        label_opts=opts.LabelOpts(formatter="{b}\n{c}", font_size=12),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
    )
)

treemap.set_series_opts(
    label_opts=opts.LabelOpts(position="inside"),
    itemstyle_opts=opts.ItemStyleOpts(border_width=0.5),
)

treemap.render("5.html")
'''



#漏斗图
data = pd.read_csv("sales_manager.csv",encoding='gbk')
sales_manager = data["sales_manager"]
sales= data["sales"]
profit = data["profit"]

a = list(zip(sales_manager, sales))
b = list(zip(sales_manager, profit))
ld1 = (
    Funnel({"theme": ThemeType.INFOGRAPHIC})
    .add("销售额", a)
    .set_global_opts(title_opts=opts.TitleOpts(title=""),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),)

)
ld2 = (
    Funnel({"theme": ThemeType.INFOGRAPHIC})
    .add("利润", b)
    .set_global_opts(title_opts=opts.TitleOpts(title=""),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),)

)


ld1.render("ld1.html")
ld2.render("ld2.html")




#旭日图
data = [
    {
        "name": "办公用品",
        "value": 949270.224,
        "children": [
            {"name": "标签", "value": 18936.54},
            {"name": "美术", "value": 33038.096},
            {"name": "器具", "value": 449744.764},
            {"name": "收纳具", "value": 214582.2},
            {"name": "系固件", "value": 20045.48},
            {"name": "信封", "value": 51941.96},
            {"name": "用品", "value": 47070.128},
            {"name": "纸张", "value": 51413.74},
            {"name": "装订机", "value": 62497.316},
        ],
    },
    {
        "name": "技术",
        "value": 937985.552,
        "children": [
            {"name": "电话", "value": 330951.32},
            {"name": "复印机", "value": 347513.264},
            {"name": "配件", "value": 150562.664},
            {"name": "设备", "value": 108958.304},
        ],
    },
    {
        "name": "家具",
        "value": 1028418.503,
        "children": [
            {"name": "书架", "value": 366969.54},
            {"name": "椅子", "value": 409393.054},
            {"name": "用具", "value": 83848.996},
            {"name": "桌子", "value": 168206.913},
        ],
    },
]

xrt = (
    Sunburst({"theme": ThemeType.INFOGRAPHIC})
    .add(
        "",
        data_pair=data,
        radius=[0, "90%"],
        highlight_policy="ancestor",
        levels=[
            {},
            {
                "r0": "15%",
                "r": "35%",
                "itemStyle": {"borderWidth": 2},
                "label": {"rotate": "tangential"},
            },
            {"r0": "40%", "r": "70%", "label": {"align": "right"}},

        ],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title=""),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=14,font_weight='bold')),)
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
)

xrt.render("xrt.html")



#标题1
# 创建数据表格
def table():
    table = Table()

    table.add(headers=['网店运营数据可视化'], rows=[], attributes={
        "style": "font-size:50px;width:1000px"
    })

    return table
table1 = table()
table1.render("table1.html",pos_left="center", pos_top="10%")

#标题2
def table():
    table = Table()

    table.add(headers=['各省销量与利润'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table2 = table()
table2.render("table2.html",pos_left="center", pos_top="10%")

#标题3
def table():
    table = Table()

    table.add(headers=['各地区销售情况'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table3 = table()
table3.render("table3.html",pos_left="center", pos_top="10%")

#标题4
def table():
    table = Table()

    table.add(headers=['各月销售情况'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table4 = table()
table4.render("table4.html",pos_left="center", pos_top="10%")

#标题5
def table():
    table = Table()

    table.add(headers=['各卖家销售情况'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table5 = table()
table5.render("table5.html",pos_left="center", pos_top="10%")

#标题6
def table():
    table = Table()

    table.add(headers=['各省市销售情况'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table6 = table()
table6.render("table6.html",pos_left="center", pos_top="10%")

#标题7
def table():
    table = Table()

    table.add(headers=['各卖家销售情况比较'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table7 = table()
table7.render("table7.html",pos_left="center", pos_top="10%")

#标题8
def table():
    table = Table()

    table.add(headers=['各类商品销售情况'], rows=[], attributes={
        "style": "font-size:20px;width:200px"
    })

    return table
table8 = table()
table8.render("table8.html",pos_left="center", pos_top="10%")


#合
page = Page(layout=Page.DraggablePageLayout)
page.add(image2,image1,map,pie,line,bar,bar1,ld1,ld2,xrt,table1,table2,table3,table4,table5,table6,table7,table8)
#page.render("数据可视化大屏.html")

page.save_resize_html('beijing.html', cfg_file='cz1.json', dest='index.html')