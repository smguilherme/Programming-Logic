#calcular qtde de latas e custo para pintar

H = float(input('Insira a altura: '))
R = float(input('Insira a raio: '))

area = (3.14*(R**2))+(2*3.14*R*H)
litro = area/3
qtde = litro/5
c = qtde*50.00

print(f'O custo é: {c:.2f} e quantidade de latas: {qtde:.2f}')
