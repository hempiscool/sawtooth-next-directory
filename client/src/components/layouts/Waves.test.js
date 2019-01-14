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
import { BrowserRouter } from 'react-router-dom';
import {shallow } from 'enzyme';



import Waves from './Waves';


describe('Waves component', () => {
  const props = {
    location: { pathname: 'route' },
    isAnimating: false,
    stopAnimation: () => { },
  };

  const newProps = {
    location: { pathname: 'alternate/route' },
    isAnimating: false,
    stopAnimation: () => { },
  };

  const wrapper = shallow(
    <BrowserRouter>
      <Waves {...props}/>
    </BrowserRouter>
  );

  it('renders without crashing', () => {
    const div = document.createElement('div');

    ReactDOM.render(
      <BrowserRouter>
        <Waves {...props}/>
      </BrowserRouter>, div
    );

    ReactDOM.unmountComponentAtNode(div);
    wrapper.instance().setState({});
  });

});
