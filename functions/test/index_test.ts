import * as Test from 'firebase-functions-test';
import * as index from '../src/index';

import { should } from 'chai';
should()

describe('function test', () => {
  it ('test', async function() {
    const test = Test();
    const wrapped = test.wrap(index.helloCall);
    const res = await wrapped({}, {});
    res.message.should.equal("Hello world");

  });
});

