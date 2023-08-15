const greet = 'Hello TypeScript'

let occupation: string
occupation = "817"

/* 在 occupation 後有一個 ?，表示該屬性不一定要存在於該物件中 */
const person: {
    name: string;
    age: number;
    occupation?: string; // 在 : 前面加上 ? 表示該屬性不是必填
  } = {
    name: 'pjchender',
    age: 32,
  };

// console.log(person)

/* 宣告型別為字串陣列*/
const devices: string[] = ['iphone', 'pixel', 'ipad', 'note 10'];
const luckyNumber1: number[] = [4, 7, 11];
const luckyNumber2: Array<number> = [4, 7, 11];

const add = (x: number, y: number): number => {
    return x + y;
  };
console.log(add(3, 5)); // 8

/* 函式不會有回傳值時使用 void */
const add2 = (x: number, y: number): void => {
    console.log(x + y);
  };

let brand: 'iphone' | 'samsung' | 'sony';

type Book = {
    name: string;
    price: number;
  };

const book1: Book = {
    name: 'Learn TypeScript',
    price: 300,
  };


// type Software = {
//     platform: string;
//     releasedAt: string;
// }

// type Hardware = {
//     RAM: string;
//     CPU: string;
// }

// type MobilePhone = Software & Hardware;

// const iphone11: MobilePhone = {
//     platform: 'ios',
//     releasedAt: '20190919',
//     RAM: '4GB',
//     CPU: 'A13',
//   };


interface Hardware {
    RAM: string;
    CPU: string;
  }

const hardware: Hardware = {
    RAM: '4GB',
    CPU: 'A13',
  };

interface Software {
    platform: string;
    releasedAt: string;
  }

interface MobilePhone extends Software, Hardware {
    price: number;
    brand: string;
  }

const iphone11: MobilePhone = {
    price: 24900,
    brand: 'apple',
    platform: 'ios',
    releasedAt: '20190919',
    RAM: '4GB',
    CPU: 'A13',
  };
  