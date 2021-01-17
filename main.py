import discord
import stock_code
import subprocess
from time import perf_counter
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("!python"))

@bot.command()
async def python(ctx):
    await ctx.send("Écrivez "+"!_ "+"suivis du nom d'une fonction ou d'un élément de python.\n"
                    "Pour avoir la liste des commandes, tapez !_liste_command")

@bot.command()
async def _liste_command(ctx):
    await ctx.send("Liste des commandes :\n"
                   "---------- Listes ----------\n"
                   "append\n"
                   "insert\n"
                   "pop\n"
                   "slice\n"
                   "sorted\n"
                   "sort\n"
                   "count\n"
                   "---------- Fonctions ----------\n"
                   "filter\n"
                   "lambda\n"
                   "map\n"
                   "----------- Type de données ----------\n"
                   "list\n"
                   "tuple\n"
                   "set\n"
                   "dict\n"
                   "int\n"
                   "str\n"
                   "frozenset\n"
                   "float\n"
                   "---------- Boucle ----------\n"
                   "for\n"
                   "while\n"
                   "---------- Script ----------\n"
                   "!_script")

@bot.command()
async def _for(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "for i in range(x):\n"
                   "\tinstruction"
                   "```"
                   "Éxecute x fois l'instruction dans la boucle")

@bot.command()
async def _while(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "while condition:\n"
                   "\tfonction"
                   "```"
                   "Passe dans la boucle tant que la condition est vrai")

@bot.command()
async def _print(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "print(variable)"
                   "```")

@bot.command()
async def _lambda(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "lambda x : expression"
                   "```"
                   "Permet de créer une fonction sans nom pour un usage précis")

@bot.command()
async def _filter(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "filter(fonction, iterable)"
                   "```"
                   "Fonction permettant de filtrer un itérable donnée en paramètre")

@bot.command()
async def _map(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "map(fonction, iterable)"
                   "```"
                   "Modifie l'itérable passé en paramètre")

@bot.command()
async def _pop(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "list.pop()"
                   "```"
                   "Enlève le dernier élément de la liste\n"
                   "```py\n"
                   "list.pop(i)"
                   "```"
                   "Enlève l'élément de la liste en position i")

@bot.command()
async def _insert(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "list.insert(x, i)"
                   "```"
                   "Insert l'élément en x en position i")

@bot.command()
async def _append(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "list.append(x)"
                   "```"
                   "Ajoute l'élément x à la fin de la liste")

@bot.command()
async def _sorted(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "sorted(list ,key = None ,reverse = False)"
                   "```"
                   "Renvoie un élément de type liste, trié en fonction de la *key*, inversé ou non en fonction du booléen après *reverse*")

@bot.command()
async def _count(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "list.count(x)"
                   "```"
                   "Compte le nombre d'occurence de x dans la liste")

@bot.command()
async def _slice(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "list[a:b:c]"
                   "```"
                   "a : élément de départ"
                   "b : élément d'arriver"
                   "c : pas")

@bot.command()
async def _sort(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   " list.sort(*, key=None, reverse=False)"
                   "```"
                   "Tri la liste en fonction de la *key*, inversé ou non en fonction du booléen après *reverse*")



@bot.command()
async def _int(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = 1\n"
                   "type(var) = int"
                   "```"
                   "Entier")

@bot.command()
async def _float(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = 1,9\n"
                   "type(var) = float"
                   "```"
                   "Nombre à virgule")

@bot.command()
async def _list(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = list()\n"
                   "var = [1,'test',[1,2],2,3]\n"
                   "type(var) = list"
                   "```")

@bot.command()
async def _tuple(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = tuple()\n"
                   "type(var) = tuple\n"
                   "var = (1,'test',[1,2],2,3)\n"
                   "```"
                   "Non modifiable")

@bot.command()
async def _dict(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "dico = dict()\n"
                   "dico[key] = value"
                   "type(var) = dict"
                   "```")

@bot.command()
async def _set(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = set()\n"
                   "type(var) = set"
                   "```")

@bot.command()
async def _frozenset(ctx):
    await ctx.send("Syntaxe :\n"
                   "```py\n"
                   "var = frozenset()\n"
                   "type(var) = frozenset\n"
                   "```\n"
                   "Non modifiable")

@bot.command()
async def _script(ctx):
    await ctx.send("Écrivez votre script python")
    #attente du message
    inter = await bot.wait_for("message")

    #verification du format puis modification du message
    if inter.content[0:5] == "```py": 
        with open("stock_code.py", "w") as fichier:
            fichier.write(str(inter.content[6:-3]))
        debut = perf_counter()
        stock = subprocess.Popen(['python3', 'stock_code.py',  'arg1 arg2 arg3 arg4'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        temp_exec = perf_counter() - debut
        stock2 = str(stock.communicate()[0])
        stock3 = str()
        print(repr(stock2))
        test1 = True
        for i in stock2[2:-3]:
            if not test1 and i == 'n':
                test1 = True
                continue
            if i != '\\':
                stock3 += i
            if i == '\\':
                test1 = False
                stock3 += '\n'

        print(repr(stock3))
        await ctx.send(stock3+"\n\nTemps d'éxecution :  "+str(temp_exec)+"s")
        with open("stock_code.py", "w") as fichier:
            fichier.write('')
    else:
        await ctx.send("Mauvais format veuillez recommencer")


if __name__ == "__main__":

    print("Lancement du bot...")

    token = "Token here"

    bot.run(token)