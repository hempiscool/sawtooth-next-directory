/* Copyright 2019 Contributors to Hyperledger Sawtooth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------- */


import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { shallow } from 'enzyme';


import * as customStore from 'customStore';
import CreatePack from './CreatePack';


const store = customStore.create();


describe('CreatePack component', () => {
  const props = {
    submit: (username, password) => { },
    userId: '',
    createPack: () => {},
    resetPackExists: () => {},
  };
  const wrapper = shallow(
    <CreatePack.WrappedComponent {...props} store={store}/>
  );

  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(
      <Provider store={store}>
        <BrowserRouter>
          <CreatePack/>
        </BrowserRouter>
      </Provider>, div
    );

    ReactDOM.unmountComponentAtNode(div);
  });

  wrapper.find('#next-approver-manage-create-pack-form').simulate(
    'change',
    { event: {} }, { name: 'name', value: '' }
  );
  wrapper.instance().createPack(props);
});
