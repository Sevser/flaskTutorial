// eslint-disable-next-line
export const SETTOKEN = (state, token) => {
  state.token = token;
  state.history.push('SETTOKEN');
};
