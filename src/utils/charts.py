import plotly.express as px

PASTEL_COLORS = px.colors.qualitative.Pastel + px.colors.qualitative.Pastel

class ChartsFactory:
    @staticmethod
    def _default_colors(colors):
        return colors if colors is not None else PASTEL_COLORS

    @staticmethod
    def create_pie_chart(data, values, names, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.pie(
            data,
            values=values,
            names=names,
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_bar_chart(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.bar(
            data,
            x=x,
            y=y,
            color=x,  # cada barra terá cor diferente
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_line_chart(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.line(
            data,
            x=x,
            y=y,
            color=x,  # cada linha terá cor diferente
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_scatter_chart(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.scatter(
            data,
            x=x,
            y=y,
            color=x,  # cada ponto terá cor diferente
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_histogram(data, x, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.histogram(
            data,
            x=x,
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_box_plot(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.box(
            data,
            x=x,
            y=y,
            color=x,  # cores diferentes para cada categoria
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_area_chart(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.area(
            data,
            x=x,
            y=y,
            color=x,  # cores diferentes para cada série
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_heatmap(data, x, y, z, title, template="plotly_dark"):
        fig = px.density_heatmap(
            data,
            x=x,
            y=y,
            z=z,
            title=title,
            template=template
        )
        return fig

    @staticmethod
    def create_funnel_chart(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.funnel(
            data,
            x=x,
            y=y,
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_treemap(data, path, values, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.treemap(
            data,
            path=path,
            values=values,
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_sunburst_chart(data, path, values, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.sunburst(
            data,
            path=path,
            values=values,
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig

    @staticmethod
    def create_violin_plot(data, x, y, title, color_discrete_sequence=None, template="plotly_dark"):
        fig = px.violin(
            data,
            x=x,
            y=y,
            color=x,  # cores diferentes para cada categoria
            title=title,
            color_discrete_sequence=ChartsFactory._default_colors(color_discrete_sequence),
            template=template
        )
        return fig
