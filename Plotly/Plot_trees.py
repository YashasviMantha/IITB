from _DUMP import me
# me.mark('D')
print('Start Prog --Debug Stat')

key_file = open('keys.txt','r')
key = key_file.read()

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# plotly.tools.set_config_file(world_readable=True,sharing='public')
# plotly.tools.set_credentials_file(username='YashasviMantha', api_key=key)

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]
# data = [trace0]

py.iplot(data, filename = 'basic-line', auto_open=False)





print('End Prog --Debug Stat')