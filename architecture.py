from graphviz import Digraph

def draw_dragonnet_panel_architecture(filename="dragonnet_panel"):
    dot = Digraph(comment="DragonNet for Panel Data", format="pdf")
    dot.attr(rankdir="LR", size="10,5")
    dot.node("X", "X\n(covariates)", shape="box", style="filled")
    dot.node("IDemb", "Individual Embedding\n(id → e_i)", shape="box", style="filled")
    dot.node("Temb", "Time Embedding\n(time → e_t)", shape="box", style="filled")
    dot.node("Attn", "Multi‑head\nAttention(e_i, e_t)", shape="box", style="filled")
    dot.node("Rep", "RepresentationNet:\n[X, e_i, e_t, Attn] → Z", shape="box", style="filled")

    dot.node("Ghat", "ĝ(·)\n(propensity head)", shape="box", style="filled")
    dot.node("Y1_head", "Ŷ(1,·)\n(treated outcome head)", shape="box", style="filled")
    dot.node("Y0_head", "Ŷ(0,·)\n(control outcome head)", shape="box", style="filled")
    dot.node("Eps", "ε\n(Targeted Reg.)", shape="ellipse", style="dashed")

    dot.edges([("X", "Rep"),
               ("IDemb", "Attn"),
               ("Temb", "Attn"),
               ("Attn", "Rep"),
               ("Rep", "Ghat"),
               ("Rep", "Y1_head"),
               ("Rep", "Y0_head"),
               ("Rep", "Eps")])

    dot.render(filename, view=True)
    return dot

draw_dragonnet_panel_architecture("dragonnet_panel")