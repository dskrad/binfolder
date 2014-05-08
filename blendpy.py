import bpy
import math
from bpy.props import BoolProperty


def splittime(secs, prec=2):
    t = float(secs)
    minutes = int(t // 60)
    t %= 60
    seconds = math.floor(t)

    t = round(t - seconds, prec)
    p = 10 ** prec
    fraction = math.floor(p * (t))
    return (minutes, seconds, fraction % p)

def countdown_timer(scene):

    # look for all font objects with _timer property
    timers = [ob.data for ob in scene.objects if ob.type == 'FONT' and ob.data.is_timer]

    for font in timers:
        secs = font["timer"]
        prec = font["prec"]
        if font.is_time:
            try:
                fmt = "{0:02,d}:{1:02d}"
                min, sec, fsec  = splittime(secs, prec=prec)
                if not prec:
                    font.body = fmt.format(min, sec)
                else:
                    fmt_prec = ".{2:0%dd}" % prec
                    fmt += fmt_prec
                    font.body = fmt.format(min, sec, fsec)
            except:
                print("EXCEPT", fmt, splittime(secs, prec=prec))
                pass
        else:
            # format the seconds only.
            # note this rounds.
            fmt = "{:,.%df}" % prec
            font.body = fmt.format(secs)
    return None


def is_timer(self, context):
    if self.is_timer:
        if "timer" not in self.keys():
            self["timer"] = 0.0
            self["prec"] = 2

            countdown_timer(context.scene)
    return None


class TimerPanel(bpy.types.Panel):
    """Timer Panel"""
    bl_label = "Countdown Timer"
    bl_idname = "FONT_PT_timer"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return (context.object and context.object.type in {'FONT'} and context.curve)
    def draw_header(self, context):
        font = context.object.data


        self.layout.prop(font, "is_timer", text="")
    def draw(self, context):
        font = context.object.data
        layout = self.layout
        if font.is_timer:
            row = layout.row()
            row.prop(font,'["timer"]', text="Seconds")
            row = layout.row()
            row.prop(font, "is_time", text="mm:ss[.prec]")
            row = layout.row()
            #frow.alert = False
            row.prop(font,'["prec"]', text="Prec")




def register():
    bpy.types.TextCurve.is_timer = BoolProperty(default=False, update=is_timer, description="Make countdown timer")
    bpy.types.TextCurve.is_time = BoolProperty(default=True, description="mm:ss[.prec]")


    bpy.app.handlers.frame_change_pre.append(countdown_timer)
    bpy.utils.register_class(TimerPanel)


def unregister():
    bpy.utils.unregister_class(TimerPanel)
    bpy.app.handlers.frame_change_pre.pop()


if __name__ == "__main__":
    register()


print("Countdown Timer")
