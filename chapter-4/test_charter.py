import charter
chart = charter.new_chart()
charter.set_title(chart, "Wild Parrot Deaths per Year")
charter.set_x_axis(chart,
                   ["2009", "2010", "2011", "2012", "2013",
                    "2014", "2015"])
charter.set_y_axis(chart, minimum=0, maximum=700,
                   labels=[0, 100, 200, 300, 400, 500, 600, 700])
charter.set_series(chart, [250, 270, 510, 420, 680, 580, 450])
charter.set_series_type(chart, "bar")
charter.generate_chart(chart, "chart.pdf")

