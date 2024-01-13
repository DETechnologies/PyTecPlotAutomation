import sys, os 
import tecplot as tp
from tecplot.constant import PlotType
troubleshooting=1

OutputFilesFolder=r"C:\Users\logan\Desktop\Capstone\Converge\WorkingFiles\DET_Converge_LP\output"
PlotVariable="PRESSURE"
# PlotVariable="TEMPERATURE"
# PlotVariable="MACH"

f=os.listdir(OutputFilesFolder)
datafilenames=[os.path.join(OutputFilesFolder,file) for file in f]

if troubleshooting:
    ### NEED TO GO IN TECPLOT GUI > SCRIPTING > ACCEPT INCOMING CONNECTIONS EACH TIME TECPLOT IS RE-OPENED
    tp.session.connect()

tp.new_layout()
dataset=tp.data.load_converge_hdf5(datafilenames)
frame = tp.active_frame()
plot = frame.plot(PlotType.Cartesian2D)

plot.contour(0).colormap_name = 'Small Rainbow'
plot.contour(0).variable = dataset.variable(PlotVariable)

plot.activate()
plot.show_contour = True

saveto=os.path.join(os.path.dirname(OutputFilesFolder),f"{PlotVariable}_Plot.mp4")
tp.export.save_time_animation_mpeg4(saveto)
    