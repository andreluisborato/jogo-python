def batalha(vida=100, vida_oponente=50):
    print(f"\n[Status] Sua vida: {vida} | Vida do oponente: {vida_oponente}")
    print("\nÉ o seu momento de agir! O que você faz?")
    print("1 - Desferir um soco pesado")
    print("2 - Executar um chute rápido")
    print("3 - Batida em retirada (Tentar Fugir)")
    ataque = input("Sua decisão: ")

    if ataque == "1":
        print("\n💥 Um golpe limpo! Seu soco atinge em cheio o peito do adversário.")
        vida_oponente -= 20
        print(f"Sua vida: {vida} | Vida do oponente: {vida_oponente}")
    elif ataque == "2":
        print("\n💨 Você se arrisca em um chute rápido, atingindo o inimigo de raspão.")
        vida_oponente -= 5
        print(f"Sua vida: {vida} | Vida do oponente: {vida_oponente}")
    elif ataque == "3":
        print("\n⚠️ Você vira as costas para escapar, mas o inimigo se projeta e te acerta em cheio!")
        vida -= 20
        print(f"Sua vida: {vida} | Vida do oponente: {vida_oponente}")

    if vida <= 0:
        print("\n💀 Seus joelhos fraquejam e a escuridão toma conta... Você foi derrotado!")
        return
    if vida_oponente <= 0:
        print("\n🏆 O inimigo cai no chão sem forças. Vitória triunfante na batalha!")
        return

    print("\n⚠️ O inimigo avança ferozmente! Como você reage ao investida dele?")
    print("1 - Tentar se esquivar para o lado")
    print("2 - Erguer a guarda e bloquear")
    print("3 - Fazer uma finta defensiva")
    escolha2 = input("Sua reação: ")

    batalha(vida, vida_oponente)

def troca_poder():
    print("\nÉ preciso ajustar sua estratégia. Deseja redefinir seu poder especial?")
    print("1 - Sim, quero trocar")
    print("2 - Não, vou manter a escolha")
    resposta1 = input("Sua escolha: ")

    if resposta1 == "1":
        print("\nSelecione uma nova habilidade especial:")
        print("1 - Colete Tático (Proteção reforçada)")
        print("2 - Velocidade Sobre-humana (Reflexos ágeis)")
        print("3 - Bloqueio Absoluto (Escudo defensivo)")
        poder = input("Escolha o número da habilidade: ")
        batalha()

    elif resposta1 == "2":
        print("\nVocê confia na sua escolha inicial... Mantenha a guarda alta e use a cabeça!")
        batalha()


print("=== TALES OF THE REALM ===")
nome = input("Antes de iniciar sua jornada, como prefere ser chamado? ")

print(f"\nSaudações, {nome}! Escolha sua habilidade inicial:")
print("1 - Colete Tático")
print("2 - Velocidade Sobre-humana")
print("3 - Bloqueio Absoluto")
poder = input("Digite o número do seu poder: ")

if poder == "1":
    print("🛡️ Colete Tático equipado com sucesso!")
elif poder == "2":
    print("⚡ Velocidade Sobre-humana ativada!")
elif poder == "3":
    print("🔰 Bloqueio Absoluto pronto para uso!")

inventario = ["Espada", "Machado", "Baú", "Armadura"]
pergunta = input("\nDeseja inspecionar o conteúdo da sua mochila agora? (1 - Verificar / 2 - Continuar jornada): ")

if pergunta == "1":
    print(f"Itens em posse: {inventario}")
elif pergunta == "2":
    print("Guardando alforje e avançando...")

print(f"\n{nome}, enquanto caminha sob a copa densa da floresta, um estalar de galhos quebra o silêncio...")
print("Uma silhueta sombria emerge das sombras com olhos reluzentes!")
print("1 - Arrancar em disparada para longe")
print("2 - Manter a posição e aguardar a aproximação")
escolha1 = input("Sua decisão imediata: ")

if escolha1 == "1":
    print("\n🏃 Você se esgueira entre as árvores e consegue despistar a criatura... por enquanto!")

if escolha1 == "2" and poder == "3":
    print("\n🔰 O monstro se projeta contra você, mas seu Bloqueio Absoluto absorve todo o impacto! Prepare-se para revidar!")
    batalha()

if escolha1 == "2" and poder != "3":
    print("\n💥 O impacto da criatura é forte demais sem uma defesa sólida! O golpe atravessa sua guarda!")
    troca_poder()