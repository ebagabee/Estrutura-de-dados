# Repositorio para Estudos de Algoritmo e Estrutura de Dados

### Array

- Espaço contido em memória que pode ser interpretado contendo vários elementos

```exemplo
let my_array: [i32; 4] = [1, 2, 3, 4];

- i32: Cada elemento do array será um inteiro de 32 bits.
- 4: Indica que o array contém exatamente 4 elementos.
```

_Buffers e Arrays_:

```js
// Exemplo

/**
 * ArrayBuffer -> Um objeto usado para armazenar dados binários de tamanho fixo.
 *
 * 8: Especifica o tamanho do buffer em bytes. Aqui estamos criando um buffer com 8 bytes
 *
 * Resultado: Um ArrayBuffer inicializado com zeros.
 */

const a = new ArrayBuffer(8);

// Saída
/*
    ArrayBuffer {
        [Uint8Contents]: <00 00 00 00 00 00 00 00>,
        byteLength: 8
    }

    Significa que temos 8 bytes (todos com valor inicial 0).
 */

// 2. Criando um Uint8Array

const a8 = new Uint8Array(a);

/*
    - Uint8Array: Uma visão sobre o ArrayBuffer que interpreta os dados como números inteiros sem sinal de 8 bits (0 - 255)
    - Estamos associando essa visão ao buffer a criado anteriormente

    Saída:

    Uint8Array(8) [0, 0, 0, 0, 0, 0, 0, 0]

    Agora podemos acessar e modificar os valores do buffer como se fosse um array de números inteiros de 8 bits.
*/

// 3. Criando um Uint32Array

const a32 = new Uint32Array(a);

/*
    Uint32Array: Outra visão sobre o mesmo ArrayBuffer, mas agora os dados são interpretados como números inteiros sem sinal de 32 bits (0 - 4,294,967,295).

    Como o buffer tem 8 bytes, essa visão permite interpretar o buffer como dois valores de 32 bits (cada valor ocupa 4 bytes)

    Saída: Uint32Array(2) [0, 0]

    Aqui o número é interpretado como dois números inteiros de 32 bits (todos inicialmente 0)
*/

// Modificando o buffer

a32[0] = 4294967295;

// Agora o maior valor possível para 32 bits é atribuído

// Saída:

/*
    ArrayBuffer {
        [Uint8Contents]: <ff ff ff ff 00 00 00 00>,
        byteLength: 8
    }
*/
```
