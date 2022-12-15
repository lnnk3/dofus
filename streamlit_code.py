import streamlit as st

header = st.container()

with header:
	st.title('Bienvenue dans ton optimisateur de parchemins !')

# On note pi le prix de l'achat d'une unité de parchemin i

p0 = st.number_input('Prix du petit parchemin :')
p1 = st.number_input('Prix du parchemin normal :')
p2 = st.number_input('Prix du grand parchemin :')
p3 = st.number_input('Prix du parchemin puissant :')

# On note pc le total de points de caractéristique détenus au cours du processus.

pc = st.number_input('Ton bonus actuel en points de caractéristiques :', min_value=0, max_value=10000, step=1)

# Soit l_v la liste des valeurs (rapport bénéfice en PC / prix d'achat) des parchemins

l_v = [1/p0, 1/p1, 1/p2, 2/p3]

# Soit l_opt la conso optimale de chacun des 4 parchemins. On initialise tout à 0.

l_opt = [0,0,0,0]

while pc < 100:
    if pc < 25:
        a = l_v.index(max(l_v))
        if a in [0,1,2]:
            pc += 1
            l_opt[a] += 1
        else:
            pc += 2
            l_opt[3] += 1
    elif 25 <= pc < 50:
        b = l_v.index(max(l_v[1:4]))
        if b in [1,2]:
            pc += 1
            l_opt[b] += 1
        else:
            pc += 2
            l_opt[3] += 1
    elif 50 <= pc < 80:
        c = l_v.index(max(l_v[2:4]))
        if c == 2:
            pc += 1
            l_opt[2] += 1
        else:
            pc += 2
            l_opt[3] += 1
    else:
        l_opt[3] += 1
        pc += 2

#st.write('Bonus PC obtenu :', pc)
#st.write('Achats optimaux :', l_opt)

st.metric(label='Bonus PC obtenu :', value=pc)
st.metric(label='Petit(s) parchemin(s)', value=l_opt[0])
st.metric(label='Parchemin(s) norma(ux)l', value=l_opt[1])
st.metric(label='Grand(s) parchemin(s)', value=l_opt[2])
st.metric(label='Parchemin(s) puissant(s)', value=l_opt[3])


