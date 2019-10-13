import {
  AnyAction,
  applyMiddleware,
  createStore,
  Dispatch,
  Middleware,
  MiddlewareAPI,
} from 'redux';
import thunk from 'redux-thunk';

import { ThunkActionOrAction } from '^/actions/types';
import rootReducer from '^/reducers';
import { StoreState } from './types';

const INITIAL_STATE: Partial<StoreState> = {
  count: 0,
  sideBarOpen: false,
};

const middleware: Array<Middleware<{}, StoreState>> = [
  thunk,
  <S>(api: MiddlewareAPI<Dispatch, S>) => (next: Dispatch) => (
    action: ThunkActionOrAction
  ) =>
    typeof action === 'function'
      ? next(action(api.dispatch, api.getState, undefined))
      : next(action),
];

const store = createStore<StoreState, AnyAction, {}, undefined>(
  rootReducer,
  INITIAL_STATE,
  applyMiddleware(...middleware)
);

export default store;
