import { GraphQLClient, gql } from 'graphql-request';

const token = "YOU THOUGHT";

fetch('https://api.start.gg/gql/alpha', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })